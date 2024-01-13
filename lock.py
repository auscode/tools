#!/usr/bin/python3
from tinyscript import *
try:
    import pikepdf
    BACKEND = "pikepdf"
except ImportError:
    import pypdf
    BACKEND = "pypdf"


__author__    = "Alexandre D'Hondt"
__version__   = "1.4"
__copyright__ = ("A. D'Hondt", 2020)
__license__   = "gpl-3.0"
__docformat__ = "md"
__examples__  = ["test_protected.pdf -p '[a-z0-9]{5}'"]
__doc__       = """
*PDF Password Bruteforcer* allows to execute a bruteforce attack on a given PDF file,
 setting a regular expression pattern for the target password.
"""

BANNER_FONT  = "tombstone"
BANNER_STYLE = {'fgcolor': "lolcat"}


def bruteforce_pdf_password(path, regex):
    if BACKEND == "pypdf":
        with open(path, 'rb') as f:
            reader = pypdf.PdfReader(f)
            for p in ts.bruteforce_re(regex):
                logger.debug(p)
                try:
                    reader.decrypt(p)
                    len(reader.pages)
                    logger.success("FOUND: " + p)
                    return True
                except pypdf.errors.FileNotDecryptedError:
                    pass
                except Exception as e:
                    logger.exception(e)
                    break
    else:
        for p in ts.bruteforce_re(regex):
            logger.debug(p)
            try:
                with pikepdf.open(path, password=p) as f:
                    logger.success("FOUND: " + p)
                    return True
            except pikepdf._qpdf.PasswordError:
                pass
            except Exception as e:
                logger.exception(e)
                break
    return False


if __name__ == '__main__':
    parser.add_argument("file", type=ts.file_exists, help="encrypted PDF file")
    parser.add_argument("-p", "--pattern", default="^[0-9a-zA-Z!-_]{1,8}", help="password pattern")
    initialize(add_time=True, noargs_action="demo", action_at_interrupt="confirm")
    logger.info("Starting PDF password bruteforce...")
    logger.handlers[-1].terminator = ""
    if not bruteforce_pdf_password(args.file, args.pattern):
        logger.failure("Password not found")
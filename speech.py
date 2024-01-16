import pyttsx3
from pydub import AudioSegment

file_path = 'new.txt'  # Replace with the path to your text file

try:
    with open(file_path, 'r') as file:
        text = file.read()

    # Initialize the text-to-speech engine
    speaker = pyttsx3.init()

    # Set the speed (rate) of speech (words per minute)
    speed = 170  # Adjust the speed according to your preference
    speaker.setProperty('rate', speed)

    pitch_level = 1.0
    speaker.setProperty('pitch',pitch_level)

    volume_level=1.0
    speaker.setProperty('volume', volume_level)


    # Set the voice (you can change the index based on available voices)
    voices = speaker.getProperty('voices')
    voice_index = 0  # Change this index to select a different voice
    speaker.setProperty('voice', voices[voice_index].id)

    # Speak the text
    speaker.say(text)
    speaker.runAndWait()
    # audio implimentation 

    temp_wav_path= 'temp.wav'
    speaker.save_to_file(text,temp_wav_path)
    speaker.runAndWait()
    

    output_file_path = 'output.mp3'

    # converting wav to mp3
    audio_segment = AudioSegment.from_wav(temp_wav_path)
    # audio_segment.export(output_file_path,format="mp3")


except Exception as e:
    print(f"An error occurred: {e}")


# import PyPDF3
# book = open('test.pdf', 'rb')
# pdfReader = PyPDF3.PdfFileReader(book)
# pages = pdfReader.numPages

# speaker = pyttsx3.init()
# for num in range(7, pages):
#     page = pdfReader.getPage(num)
#     text = page.extractText()
#     speaker.say(text)
#     speaker.runAndWait()

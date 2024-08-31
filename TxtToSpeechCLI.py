import pyttsx3
#to install this library use 'pip install pyttx3'

def text_to_speech(text, rate = 120):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)  # Adjust speech rate (speed)
    engine.say(text)
    engine.runAndWait()

text = input("Enter the text you want to convert to speech: \n")
rate = int(input("Enter the speed of voice [eg.(1x= 120)|(0.5x= 200)|(2x= 400)]: \n"))
text_to_speech(text, rate)

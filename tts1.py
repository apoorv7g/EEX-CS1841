# testing tts
import pyttsx3
tts = pyttsx3.init()
txt = input("Enter a String")
tts.say(txt)
tts.runAndWait()  

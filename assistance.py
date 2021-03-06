from ast import If
from datetime import datetime
import pyttsx3
import speech_recognition as sr

# Video Reference
# https://www.youtube.com/watch?v=Lp9Ftuq2sVI&t=1220s

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[1].id)
voices = engine.setProperty('voice', voices[1].id)

def change_voice(engine, language, gender='VoiceGenderFemale'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Evening")

    else:
        speak("Good Night")


def acceptCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print("User Said: \n")
        print(query)

    except Exception as e:
        print(e)
        print("Say that again...")
        return "None"


if __name__ == "__main__":
    change_voice(engine, "en_US", "VoiceGenderFemale")
    speak("Hello, I am Cybolite Assistant")
    #speak("My God is Mr. Shivash")
    acceptCommand()


# https://www.youtube.com/watch?v=46pBeyHKQuQ

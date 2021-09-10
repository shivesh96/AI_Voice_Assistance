from ast import If
from datetime import datetime
import pyttsx3

# Video Reference
# https://www.youtube.com/watch?v=Lp9Ftuq2sVI&t=1220s

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)


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


if __name__ == "__main__":
    speak("Shivesh is a good boy")


# https://www.youtube.com/watch?v=46pBeyHKQuQ

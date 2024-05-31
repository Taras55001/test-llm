#!/usr/bin/env python3
import os
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import speech_recognition as sr
except ImportError:
    install("SpeechRecognition")
    import speech_recognition as sr

try:
    import pyttsx3
except ImportError:
    install("pyttsx3")
    import pyttsx3

def recognize_speech_from_microphone():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Будь ласка, скажіть щось...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="uk-UA")
        print("Ви сказали: " + text)
        return text
    except sr.UnknownValueError:
        print("Розпізнавач не зміг зрозуміти аудіо")
        return None
    except sr.RequestError:
        print("Помилка сервісу розпізнавання мови")
        return None

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    recognized_text = recognize_speech_from_microphone()
    if recognized_text:
        speak_text(recognized_text)

#!/usr/bin/env python3
import subprocess
import sys
import time
from test import llm_request

exit_keys = ["закінчити програму","завершити програму","кінець програми"]
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


def recognize_speech_from_microphone(recognizer, microphone, timeout=None):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=timeout)
            text = recognizer.recognize_google(audio, language="uk-UA")
            return text.lower()
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            print("Помилка сервісу розпізнавання мови")
            return None


def speak_text(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "David" in voice.name:
            engine.setProperty(voice.name,voice.id)
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Система активна. Скажіть 'вероніка', щоб почати. Скажіть 'закінчити програму', щоб завершити роботу.")
    while True:
        text = recognize_speech_from_microphone(recognizer, microphone, timeout=5)
        if text:
            last_spoke_time = time.time()
            if "вероніка" in text:
                print("Тригерне слово розпізнано, починаю запис...")
                print("Ви сказали: " + text)
                full_text = [text.removeprefix("вероніка")]
                final_text = llm_request(full_text, 256)
                print(final_text)
                speak_text(final_text)
                print(
                    "Система активна. Скажіть 'вероніка', щоб почати. Скажіть 'закінчити програму', щоб завершити роботу.")
            elif any(phrase in text for phrase in exit_keys):
                print("Завершення програми...")
                speak_text("Завершення програми")
                break
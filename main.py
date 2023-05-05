import pyaudio
import wave
import speech_recognition as sr
from googletrans import Translator
import openai
import os
import language
import pyttsx3

translator = Translator()
engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.kyoko')

def gpt3_response(question):
    openai.api_key = ""
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"{language.languages[language.code()]}: {question}\nGPT-3:",
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = response.choices[0].text
    return answer.strip()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_microphone():
    print(f"Say something in {language.languages[language.code()]}:")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit=5)
    try:
        return r.recognize_google(audio, language=language.code())
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        print(f"Could not connect to the voice recognition service; {e}")
        return ""

keywords = ["did not understand", "confused", "do not know"]
CHUNK = 1024  
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
)

while True:
    question = listen_microphone()
    speak(question)
    
    if any(keyword in question for keyword in keywords):
        print("Sorry, I did not understand your question. Please try rephrasing it.")
        continue
        
    answer = gpt3_response(question)
    print(f"GPT-3: {answer}")
    
    if any(keyword in answer for keyword in keywords):
        print("Sorry, I did not understand your question. Please try rephrasing it.")
        continue
    
    if language.languages[language.code()] == 'en-US':
        continue
    else:
        translation = translator.translate(answer, src=f"{language.languages[language.code()]}", dest='en')
        print(f"Translation to English: {translation.text}")

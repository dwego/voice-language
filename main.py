import pyaudio
import wave
from google.cloud import texttospeech, speech_v1 as speech
from googletrans import Translator
import openai
import os
import idioma

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "upbeat-beach-383103-d65b2c34661a.json"
client = texttospeech.TextToSpeechClient()
client_speech = speech.SpeechClient()
translator = Translator()

def gpt3_resposta(pergunta):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"{idioma.linguagens[idioma.codigo_selecionado]}: {pergunta}\nGPT-3:",
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    resposta = response.choices[0].text
    return resposta.strip()

def falar_japones(texto):
    synthesis_input = texttospeech.SynthesisInput(text=texto)
    voice = texttospeech.VoiceSelectionParams(
        language_code=f"idioma.codigo_selecionado", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open("resposta.mp3", "wb") as out:
        out.write(response.audio_content)

    chunk = 1024  
    wf = wave.open("resposta.mp3", "rb")
    p = pyaudio.PyAudio()
    stream = p.open(
        format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True,
    )

    data = wf.readframes(chunk)

    while data:
        stream.write(data)
        data = wf.readframes(chunk)

    stream.stop_stream()
    stream.close()
    p.terminate()

def ouvir_microfone():
    print(f"Diga algo em {idioma.linguagens[idioma.codigo_selecionado]}:")
    res = client_speech.recognize(
        config=speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code=f"{idioma.codigo_selecionado}",
        ),
        audio=speech.RecognitionAudio(content=stream.read(CHUNK)),
    )
    try:
        return res.results[0].alternatives[0].transcript
    except IndexError:
        return ""

palavras_chave = ["não entendi", "confuso", "não sei"]
CHUNK = 1024  
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
)

while True:
    pergunta = ouvir_microfone()
    falar_japones(pergunta)
    
    if any(palavra in pergunta for palavra in palavras_chave):
        print("Desculpe, não entendi sua pergunta. Por favor, tente reformulá-la.")
        continue
        
    resposta = gpt3_resposta(pergunta)
    print(f"GPT-3: {resposta}")
    
    if any(palavra in resposta for palavra in palavras_chave):
        print("Desculpe, não entendi sua pergunta. Por favor, tente reformulá-la.")
        continue
    
    traducao = translator.translate(resposta, src='ja', dest='pt')
    print(f"Tradução para o português: {traducao.text}")
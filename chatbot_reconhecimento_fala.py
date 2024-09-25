#%% Bibliotecas
# pip install --upgrade wheel
from io import BytesIO
from pathlib import Path

import speech_recognition as sr
from playsound import playsound

import openai
from dotenv import load_dotenv, find_dotenv

#%% Conecta com a API
_ = load_dotenv(find_dotenv())
client = openai.Client()

#%% Arquivo para salvar o audio gerado
ARQUIVO_AUDIO = 'fala_assistant.mp3'

#%% Funções
# Define a função de reconhecimento de voz
recognizer = sr.Recognizer()
def grava_audio():
    with sr.Microphone() as source:
        print('Ouvindo...')
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    return audio

# Função para converter a fala em texto
def transcricao_audio(audio):
    wav_data = BytesIO(audio.get_wav_data())
    wav_data.name = 'audio.wav'
    transcricao = client.audio.transcriptions.create(
        model='whisper-1',
        file=wav_data,
    )
    return transcricao.text

# Função para gerar o texto da resposta da IA
def completa_texto(mensagens):
    resposta = client.chat.completions.create(
        messages=mensagens,
        model='gpt-3.5-turbo-0125',
        max_tokens=1000,
        temperature=0
    )
    return resposta

# Função para criar o audio da respostas
def cria_audio(texto):
    if Path(ARQUIVO_AUDIO).exists():
        Path(ARQUIVO_AUDIO).unlink()
    resposta = client.audio.speech.create(
        model='tts-1',
        voice='onyx',
        input=texto
    )
    resposta.write_to_file(ARQUIVO_AUDIO)

# Função para tocar o audio
def roda_audio():
    playsound(ARQUIVO_AUDIO)


if __name__ == '__main__':

    mensagens = []

    while True:
        audio = grava_audio()
        transcricao = transcricao_audio(audio)
        mensagens.append({'role': 'user', 'content': transcricao})
        print(f'User: {mensagens[-1]["content"]}')
        resposta = completa_texto(mensagens)
        mensagens.append({'role': 'assistant', 'content': resposta.choices[0].message.content})
        print(f'Assistant: {mensagens[-1]["content"]}')
        cria_audio(mensagens[-1]["content"])
        roda_audio()

import asyncio
import os
from deepgram import Deepgram
from dotenv import load_dotenv 


# Inicializando o cliente Deepgram
dg_client = Deepgram(os.getenv("API_KEY_DEEPGRAM"))

#Transformando a transcrição num arquivo .txt
def txt_transcricao(texto, filename):
    with open(filename, "w") as file:
        file.write(texto)

# Função para realizar a transcrição
async def transcrever_audio(audio_path):
    with open(audio_path, 'rb') as audio_file:
        # Transcrição do áudio
        source = {'buffer': audio_file, 'mimetype': 'audio/wav'}
        response = await dg_client.transcription.prerecorded(source, {'punctuate': True})
        return response['results']['channels'][0]['alternatives'][0]['transcript']

#iniciando o dotenv
def configure():
    load_dotenv()
# Chamada da função
async def main():
    audio_path = 'kamala'
    configure()
    transcricao = await transcrever_audio(f'audio/{audio_path}.wav')
    txt_transcricao(transcricao, f"{audio_path}.txt")
    print(f"Transcrição: {transcricao}")

# Executa a transcrição
asyncio.run(main())

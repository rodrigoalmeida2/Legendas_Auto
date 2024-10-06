import os, re, subprocess
from dotenv import load_dotenv
from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)
from deepgram_captions import DeepgramConverter, srt
from google.cloud import translate_v2 as translate

load_dotenv()

# Inicia o client Deepgram
deepgram = DeepgramClient(os.getenv("API_KEY_DEEPGRAM"))

# Extrai o áudio do vídeo
def extrai_audio(video_path, audio_output_path):
    """Extrai o áudio de um vídeo usando FFmpeg"""
    comando = f"ffmpeg -i {video_path} -q:a 0 -map a {audio_output_path}"
    subprocess.run(comando, shell=True)

# Transcreve o áudio
def transcricao(audio_path, source_lg):
    try:
        with open(audio_path, "rb") as file:
            buffer_data = file.read()
        # Conteudo do áudio
        payload: FileSource = {
            "buffer": buffer_data,
        }
        # Coloca as opções do áudio
        options = PrerecordedOptions(
            model="whisper-medium",
            language=source_lg,
            smart_format=True,
        )
        # Chama a função para transcrever
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
        return response
    
    except Exception as e:
        print(f"Exception: {e}")

# Cria um arquivo srt para as legendas
def cria_srt(response):
    # Pega a transcrição, passa para o DeepgramConverter, que devolve um srt
    transcription = DeepgramConverter(response)
    # Para srt 
    captions = srt(transcription)
    # Transforma os bytes em uma string usando a codificação "utf-8"
    if isinstance(captions, bytes):
        captions = captions.decode("utf-8")

    return captions

# Traduz a legenda usando API do googlecloud
def translate_text(target: str, text: str) -> dict:
    # Inicia o client
    translate_client = translate.Client()
    # Transforma os bytes em uma string usando a codificação "utf-8"
    if isinstance(text, bytes):
        text = text.decode("utf-8")
    # Pega o resultado da tradução
    result = translate_client.translate(text, target_language=target)
    
    return result["translatedText"]

# Transforma o texto traduzido em um arquivo e troca "&gt;" por ">" no texto
def retira_gt(result, output_srt):
    # Escreve o conteúdo inicial no arquivo
    with open("td.srt", "w", encoding="utf-8") as srt:
        srt.write(result)
    # Lê o arquivo, faz a substituição e salva o resultado em outro arquivo
    with open("td.srt", 'r', encoding="utf-8") as entrada, open(output_srt, 'w', encoding="utf-8") as saida:
        for linha in entrada:
            linha_modificada = linha.replace("&gt;", ">")
            saida.write(linha_modificada)
    # remove o arquivo temporário texto traduzido
    os.remove("td.srt")

# Reescreve o srt traduzido num formato srt
def organizar_srt_linha_unica(input_srt, output_srt):
    with open(input_srt, "r", encoding="utf-8") as entrada, open(output_srt, 'w', encoding="utf-8") as saida:
        texto = entrada.read()
        # Separa o conteúdo único em blocos de legenda (id, timestamps, e texto)
        padrao = r'(\d+)\s+(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\s+(.+?)(?=\d+\s+\d{2}:\d{2}:\d{2},\d{3} -->|\s*\Z)'
        legendas = re.findall(padrao, texto)

        # Escreve as legendas organizadas no novo arquivo
        for i, legenda in enumerate(legendas):
            saida.write(f"{i+1}\n{legenda[1]} --> {legenda[2]}\n{legenda[3]}\n\n")

# Adiciona as legendas no vídeo
def add_legenda_no_video(video_path, srt_path, output_video_path):
    """Adiciona legendas ao vídeo usando FFmpeg"""
    comando = f"ffmpeg -i {video_path} -vf subtitles={srt_path} {output_video_path}"
    subprocess.run(comando, shell=True)

# main def para chamar todas as funções
def processa_video(video_path, source_lg, target_lg):
    # 1. Extrai áudio do vídeo
    audio_path = os.path.splitext(video_path)[0] + ".wav"
    extrai_audio(video_path, audio_path)
    # 2. Faz a transcrição do arquivo
    response = transcricao(audio_path, source_lg)
    # Para arquivos que não solicitam tradução
    if source_lg == target_lg:
        # 3. Cria um arquivo srt
        captions = cria_srt(response)
        srt_path = os.path.splitext(video_path)[0] + ".srt"
        with open(srt_path, "w", encoding="utf-8") as srt:
            srt.write(captions)
        # 4. Adiciona legenda no video
        output_video_path = os.path.splitext(video_path)[0] + "_subtitled.mp4"
        add_legenda_no_video(video_path, srt_path, output_video_path)    
    # Para arquivos que solicitam tradução
    else:
        # 3. Cria um arquivo srt
        captions = cria_srt(response)
        # 4. Traduz srt
        result = translate_text(target_lg, captions)
        # 5. Cria o srt e subistitui "&gt;" por ">"
        srt_path_linha = os.path.splitext(video_path)[0] + "_linha.srt"
        retira_gt(result, srt_path_linha)
        # 6. Organiza srt
        srt_path = os.path.splitext(video_path)[0] + ".srt"
        organizar_srt_linha_unica(srt_path_linha, srt_path)
        # 7. Adiciona legenda no video
        output_video_path = os.path.splitext(video_path)[0] + "_subtitled.mp4"
        add_legenda_no_video(video_path, srt_path, output_video_path)
        os.remove(srt_path_linha)


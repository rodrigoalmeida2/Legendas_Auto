<div align="center">
  
[![English](https://img.shields.io/badge/lang-English-blue.svg)](https://github.com/rodrigoalmeida2/Legendas_Auto/blob/main/README.en.md)


# Geração de Legendas Automáticas com Tradução 📽️🎧

Este projeto realiza a geração de Legendas com opção de tradução para outras línguas. 

</div>

## Índice 📇

  1. [Sobre o Projeto](#sobre-o-projeto)
  2. [Ferramentas Utilizadas](#ferramentas-utilizadas)
  3. [Como Funciona](#como-funciona)
  4. [Como Usar](#como-usar)
  5. [Interface](#interface)
  6. [Exemplo](#exemplo)
  8. [Licença](#licença)

---

## Sobre o Projeto 
📜  
Este projeto foi criado para facilitar o entendimento de videos, gerando automaticamente legendas sincronizadas. O sistema ultiliza **FFmpeg** para extrair o áudio do vídeo, **Deepgram API** para transcrever o áudio, uma **Cloud Translation API** para traduzir o texto transcrito e uma interface feita em **Streamlit**. Com essas ferramentas é possível processar arquivos de vídeo, converter a fala em texto e criar legendas automáticas com alta precisão.

## Ferramentas Utilizadas 
🪛⚙️🔧  
- **Python**: 🐍
  - **Função**: Linguagem principal usada no projeto para gerenciar a integração com a API, manipular arquivos e processar as transcrições.
  - **Uso**: O código Python se comunica com a API do Deepgram para obter as transcrições e organiza os dados para a geração de legendas.

- **Deepgram API**: 🦑
  - **Função**: Serviço de transcrição de áudio baseado em IA, capaz de processar arquivos de áudio ou vídeo e converter fala em texto com alta precisão.
  - **Uso**: O áudio é enviado para a API, que retorna a transcrição já pontuada e organizada.

- **Cloud Translation API**: 🌍
  - **Função**: Usa a tradução automática neural do Google para permitir que você traduza dinamicamente textos por meio da API usando um modelo personalizado pré-treinado do Google ou um modelo de linguagem grande (LLM) especializado em tradução.
  - **Uso**: Um texto é enviado para a API com o código da lingua que se deseja, retornando o texto traduzido.

- **Streamlit**: 💻
  - **Função**: Streamlit é um FrameWork Python de código aberto para criação de sites dinâmicos com apenas algumas linhas de código.
  - **Uso**: Basta rodar o script onde ele esta implementado.

- **FFmpeg**: 🎬
  - **Função**: FrameWork de multimídia capaz de decodificar, codificar, transcodificar, multiplexar, demultiplexar, transmitir, aplicar filtros e reproduzir praticamente qualquer formato de mídia criado por humanos e máquinas.
  - **Uso**: Um arquivo multimídia é inserido com comandos, e é retornado com os resultados deste comando. 

## Como Funciona 
🛠️  
1. **Entrada de Dados**:
   - O usuário carrega um arquivo de vídeo para o sistema
   - Escolhe a língua de origem do vídeo e a língua na qual ele quer a legenda

2. **Processamento**:
   - Extrai o áudio do vídeo com **FFmpeg**
   - O áudio é enviado para a **API do Deepgram**, retornando a transcrição em formato **srt**
   - Usando a **Cloud Translation API**, é passado o arquivo **srt** e devolvido ele traduzido
   - O arquivo é passado ao **FFmpeg**, colocado no vídeo e salvo
  
5. **Saída**:
   - - Um botão de download com o arquivo aparece e o usuário pode, então, baixar

## Como Usar 
🤳🏽
### 1. Construindo o Ambiente

  1. Abra um terminal na pasta do seu projeto e execute o comando:
      ```bash
      git clone https://github.com/rodrigoalmeida2/Legendas_Auto.git
  2. Crie um ambiente virtual:
      ```bash
      python -m venv nome_da_sua_venv
  3. Inicie sua venv:
      ```bash
      nome_da_sua_venv/Scripts/Activate
  4. Instalar os FrameWorks e ferramentas necessárias:
      ```bash
      pip install -r requirements.txt

### 2. Instalando o FFmpeg e Configurando:
  
  Instale o Chocolatey:
  
  1. Abra o PowerShell como Administrador e execute o seguinte comando para instalar o Chocolatey:
  ```bash
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
  2. Instale o FFmpeg:
      1. Após instalar o Chocolatey, execute o seguinte comando no PowerShell:
      ```bash
      choco install ffmpeg
  3. Após a instalação, você pode verificar se o FFmpeg foi instalado corretamente:
      ```bash
      ffmpeg -version
  4. Método 2: Instalação Manual:
      1. Acesse [Instalação manual FFmpeg](https://youtu.be/Q267RF1I3GE)
  
### 3. Configurar as APIs
-
    1. **Deepgram**
        1. Acesse o [site do Deepgram](https://deepgram.com).
        2. Crie uma conta e obtenha sua chave de API.
    2. **Google Cloud**
        1. Acesse o [Google Cloud](cloud.google.com)
        2. crie sua conta, acesse o console do cloud, crie um projeto
        3. Na barra de pesquisa do projeto, digite **Cloud Translation API**
        4. Quando abrir, clique em **enable**, Aparecerá a opção gerenciar, clique nela, depois vá até **Credentials**
        5. Clique em **CREATE CREDENTIALS**, **API Key**

### 4. Usar suas chaves
  - Crie um arquivo ```.env```, coleque suas chaves e depois use o dotenv para usa-lás ou coloque direto no código
    
### 5. Rode o código
  ```bash
  streamlit run main.py
  ```
### 6. Limite de Upload
  - O **Streamlit** só permite 200 MB de upload. Se você desejar fazer um upload maior que o limite, passe este comando na hora de rodar o código:
  ```bash
  streamlit run main.py --server.maxUploadSize 200
  ```

## Interface

![Interface Streamlit](https://github.com/user-attachments/assets/fccc882b-f43d-4e64-b6a7-e523cbc10989)

## Exemplo

https://github.com/user-attachments/assets/04599e8c-f2ef-45a3-bfa5-46f83a518d3a



## Licença
- Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

# Geração de Legendas Automáticas com Tradução 📽️🎞️🎧

Este projeto realiza a geração de Legendas com opção de tradução para outras línguas. 

## Índice 📇

1. [Sobre o Projeto](#sobre-o-projeto)
2. [Ferramentas Utilizadas](#ferramentas-utilizadas)
3. [Como Funciona](#como-funciona)
4. [Como Usar](#como-usar)
5. [Interface](#interface)
6. [Contribuição](#contribuição)
7. [Contato](#contato)
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

- Abra um terminal na pasta do seu projeto e execute o comando:
  ```bash
  git clone https://github.com/rodrigoalmeida2/Legendas_Auto.git
- Crie um ambiente virtual:
  ```bash
  python -m venv nome_da_sua_venv
- Inicie sua venv:
  ```bash
  nome_da_sua_venv/Scripts/Activate
- Instalar os FrameWorks e ferramentas necessárias:
  ```bash
  pip install -r requirements.txt

### 2. Instalando o FFmpeg e Configurando:
  
  - Instale o Chocolatey:
  
  - Abra o PowerShell como Administrador e execute o seguinte comando para instalar o Chocolatey:
  ```bash
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
  - Instale o FFmpeg:
    - Após instalar o Chocolatey, execute o seguinte comando no PowerShell:
    ```bash
    choco install ffmpeg
  - Após a instalação, você pode verificar se o FFmpeg foi instalado corretamente:
    ```bash
    ffmpeg -version
  - Método 2: Instalação Manual:
    - Acesse [Instalação manual FFmpeg](https://youtu.be/Q267RF1I3GE)
  
### 3. Configurar as APIs

- **Deepgram**
  - Acesse o [site do Deepgram](https://deepgram.com).
  - Crie uma conta e obtenha sua chave de API.
- **Google Cloud**
  - Acesse o [Google Cloud](cloud.google.com)
  - crie sua conta, acesse o console do cloud, crie um projeto
  - Na barra de pesquisa do projeto, digite **Cloud Translation API**
  - Quando abrir, clique em **enable**, Aparecerá a opção gerenciar, clique nela, depois vá até **Credentials**
  - Clique em **CREATE CREDENTIALS**, **API Key**

### 4. Usar suas chaves
  - Crie um arquivo ```.env```, coleque suas chaves e depois use o dotenv para usa-lás ou coloque direto no código
    
### 5. Rode o código
  ```bash
  streamlit run main.py
  ```


## Interface

![Interface Streamlit](https://github.com/user-attachments/assets/fccc882b-f43d-4e64-b6a7-e523cbc10989)


## Contribuição  
🙏🏼
Contribuições são bem-vindas! Siga os passos abaixo:  

  - Crie uma branch com a sua feature
    ```bash
    git checkout -b feature/nova-feature
  - Commit suas mudanças
    ```bash
    git commit -m "Adiciona nova feature"
  - Envie para o repositório original
    ```bash
    git push origin feature/nova-feature
  - Abra um Pull Request.

## Contato  
<p align="left">
  <a href="mailto:rodrigoalmeida350.ra@gmail.com" title="Gmail">
  <img src="https://img.shields.io/badge/-Gmail-FF0000?style=flat-square&labelColor=FF0000&logo=gmail&logoColor=white&link=LINK-DO-SEU-GMAIL" alt="Gmail"/></a>
  <a href="https://www.linkedin.com/in/rodrigo101/" title="LinkedIn">
  <img src="https://img.shields.io/badge/-Linkedin-0e76a8?style=flat-square&logo=Linkedin&logoColor=white&link=LINK-DO-SEU-LINKEDIN" alt="LinkedIn"/></a>
  <a href="https://www.instagram.com/rodrigoalmeida2k/" title="Instagram">
  <img src="https://img.shields.io/badge/-Instagram-DF0174?style=flat-square&labelColor=DF0174&logo=instagram&logoColor=white&link=LINK-DO-SEU-INSTAGRAM" alt="Instagram"/></a>
</p>

## Licença
- Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

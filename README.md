# Geração de Legendas Automáticas com Tradução 🎧🎬

Este projeto realiza a geração de Legendas com opção de tradução para outras línguas. 

## Índice

1. [Sobre o Projeto](#sobre-o-projeto)
2. [Ferramentas Utilizadas](#ferramentas-utilizadas)
3. [Como Funciona](#como-funciona)
4. [Como Usar](#como-usar)
5. [Possíveis Expansões](#possíveis-expansões)
6. [Contribuição](#contribuição)
7. [Contato](#contato)
8. [Licença](#licença)

---

## Sobre o Projeto

Este projeto foi criado para facilitar o entendimento de videos, gerando automaticamente legendas sincronizadas. O sistema ultiliza **FFmpeg** para extrair o áudio do vídeo, **Deepgram API** para transcrever o áudio, uma **Cloud Translation API** para traduzir o texto transcrito e uma interface feita em **streamlit**. Com essas ferramentas é possível processar arquivos de vídeo, converter a fala em texto e criar legendas automáticas com alta precisão.

## Ferramentas Ultilizadas

- **Python**:
  - **Função**: Linguagem principal usada no projeto para gerenciar a integração com a API, manipular arquivos e processar as transcrições.
  - **Uso**: O código Python se comunica com a API do Deepgram para obter as transcrições e organiza os dados para a geração de legendas.

- **Deepgram API**:
  - **Função**: Serviço de transcrição de áudio baseado em IA, capaz de processar arquivos de áudio ou vídeo e converter fala em texto com alta precisão.
  - **Uso**: O áudio é enviado para a API, que retorna a transcrição já pontuada e organizada.

- **Cloud Translation API**:
  - **Função**: Usa a tradução automática neural do Google para permitir que você traduza dinamicamente textos por meio da API usando um modelo personalizado pré-treinado do Google ou um modelo de linguagem grande (LLM) especializado em tradução.
  - **Uso**: Um texto é enviado para a API com o código da lingua que se deseja, retornando o texto traduzido.

- **Streamlit**:
  - **Função**: Streamlit é um FrameWork Python de código aberto para criação de sites dinâmicos com apenas algumas linhas de código.
  - **Uso**: Basta rodar o script onde ele esta implementado.

- **FFmpeg**:
  - **Função**: FrameWork de multimídia capaz de decodificar, codificar, transcodificar, multiplexar, demultiplexar, transmitir, aplicar filtros e reproduzir praticamente qualquer formato de mídia criado por humanos e máquinas.
  - **Uso**: Um arquivo multimídia é inserido com comandos, e é retornado com os resultados deste comando. 

## Como Funciona

1. **Entrada de Dados**:
   - O usuário carrega um arquivo de vídeo para o sistema
   - Escolhe a língua de origem do vídeo e a língua na qual ele quer a legenda

2. **Processamento**:
   - Extrai o áudio do vídeo com ffmpeg
   - O áudio é enviado para a **API do Deepgram**, retornando a transcrição em formato **srt**
   - Usando a **Cloud Translation API**, é passado o arquivo **srt** e devolvido ele traduzido
   - O arquivo é passado ao ffmpeg, colocado no vídeo e salvo
  
5. **Saída**:
   - - Um botão de download com o arquivo aparece e o usuário pode, então, baixar

## Como Usar

### 1. Configurar a API

- Acesse o [site do Deepgram](https://deepgram.com) e obtenha sua chave de API.
- No código, substitua o valor `DEEPGRAM_API_KEY` pela sua chave pessoal.

### 2. Instalar as Dependências

Execute o seguinte comando para instalar as dependências necessárias:

```bash
pip install -r requirements.txt
```
### 3. Usar sua chave
Crie um arquivo ```.env``` e coleque sua chave e depois use o dotenv para usa-lá
```bash
import os
from dotenv import load_dotenv 

# Inicializando o cliente Deepgram
dg_client = Deepgram(os.getenv("API_KEY_DEEPGRAM"))
```
### 4. Rode o código
```bash
python main.py
```
### 4. Visualizar o Resultado
A transcrição será exibida no console. Ela também é salva num arquivo .txt

## Possíveis Expansões
- Este projeto pode ser facilmente expandido para:
  1. Suportar múltiplos formatos de áudio e vídeo.
  2. Gerar arquivos de legendas em formato .srt ou .vtt para integração direta com plataformas de vídeo.
  3. Integrar com ferramentas de edição de vídeo para adicionar automaticamente as legendas ao conteúdo.
  4. Implementar suporte a diferentes idiomas, dependendo das capacidades da API.

## Contribuição  🙏🏼
Contribuições são bem-vindas! Siga os passos abaixo:  

  - Faça um fork do repositório.
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

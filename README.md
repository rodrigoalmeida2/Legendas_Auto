# Transcrição de Áudios em Legendas 🎧🎬

Este projeto realiza a transcrição automática de áudios para gerar legendas. Usando a **Deepgram API**, é possível processar arquivos de áudio, converter a fala em texto e criar legendas automáticas com alta precisão.

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

Este projeto foi criado para facilitar a transcrição de áudios e vídeos, gerando automaticamente legendas sincronizadas. Ele utiliza a **API do Deepgram** para realizar a transcrição de forma eficiente e precisa, com suporte a múltiplos formatos de áudio e opções de pontuação automática.

## Ferramentas Utilizadas

- **Deepgram API**:
  - **Função**: Serviço de transcrição de áudio baseado em IA, capaz de processar arquivos de áudio ou vídeo e converter fala em texto com alta precisão.
  - **Uso**: O áudio é enviado para a API, que retorna a transcrição já pontuada e organizada.
  
- **Python**:
  - **Função**: Linguagem principal usada no projeto para gerenciar a integração com a API, manipular arquivos e processar as transcrições.
  - **Uso**: O código Python se comunica com a API do Deepgram para obter as transcrições e organiza os dados para a geração de legendas.

- **Asyncio**:
  - **Função**: Biblioteca que permite o processamento assíncrono de várias transcrições ao mesmo tempo, aumentando a eficiência.
  - **Uso**: Processa várias requisições à API simultaneamente, sem bloquear o código.

## Como Funciona

1. **Entrada de Áudio**:
   - O usuário carrega um arquivo de áudio para o sistema.
  
2. **Processamento**:
   - O áudio do vídeo é extraído e enviado para a **API do Deepgram**.
   - A API realiza a transcrição do áudio, reconhecendo a fala e adicionando pontuação.

3. **Sincronização de Legendas**:
   - A transcrição é associada aos tempos do áudio, gerando legendas automáticas.
  
4. **Saída**:
   - O arquivo de vídeo é atualizado com as legendas ou a transcrição é salva separadamente.

## Como Usar

### 1. Configurar a API

- Acesse o [site do Deepgram](https://deepgram.com) e obtenha sua chave de API.
- No código, substitua o valor `DEEPGRAM_API_KEY` pela sua chave pessoal.

### 2. Instalar as Dependências

Execute o seguinte comando para instalar as dependências necessárias:

```bash
pip install deepgram-sdk==2.* python-dotenv
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

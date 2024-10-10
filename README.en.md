<div align="center">

# Automatic Subtitle Generation with Translation 📽️🎧

This project generates subtitles with the option of translating them into other languages.

</div>

## Index 📇

1. [About the Project](#about-the-project)
2. [Tools Used](#tools-used)
3. [How It Works](#how-it-works)
4. [How to Use](#how-to-use)
5. [Interface](#interface)
6. [Contribution](#contribution)
7. [Contact](#contact)
8. [License](#license)

---

## About the Project
📜
This project was created to make it easier to understand videos by automatically generating synchronized subtitles. The system uses **FFmpeg** to extract audio from video, **Deepgram API** to transcribe audio, a **Cloud Translation API** to translate transcribed text, and an interface made in **Streamlit**. With these tools, it is possible to process video files, convert speech to text, and create automatic subtitles with high accuracy.

## Tools Used
🪛⚙️🔧
- **Python**: 🐍
  - **Function**: Main language used in the project to manage integration with the API, manipulate files, and process transcripts.
  - **Usage**: The Python code communicates with the Deepgram API to obtain transcripts and organizes the data for generating subtitles.

- **Deepgram API**: 🦑
  - **Function**: AI-based audio transcription service capable of processing audio or video files and converting speech to text with high accuracy. - **Usage**: The audio is sent to the API, which returns the already scored and organized transcript.

- **Cloud Translation API**: 🌍
  - **Function**: Uses Google's neural machine translation to allow you to dynamically translate texts through the API using a custom pre-trained Google model or a large language model (LLM) specialized in translation.
  - **Usage**: A text is sent to the API with the code of the desired language, returning the translated text.

- **Streamlit**: 💻
  - **Function**: Streamlit is an open-source Python Framework for creating dynamic websites with just a few lines of code.
  - **Usage**: Just run the script where it is implemented.

- **FFmpeg**: 🎬
  - **Function**: Multimedia Framework capable of decoding, encoding, transcoding, multiplexing, demultiplexing, streaming, applying filters and playing virtually any media format created by humans and machines.
  - **Usage**: A multimedia file is input with commands, and is returned with the results of this command.

## How It Works
🛠️
1. **Data Input**:
    - The user uploads a video file to the system
    - Chooses the source language of the video and the language in which he wants the subtitles

2. **Processing**:
    - Extracts the audio from the video with **FFmpeg**
    - The audio is sent to the **Deepgram API**, returning the transcription in **srt** format
    - Using the **Cloud Translation API**, the **srt** file is passed and returned translated
    - The file is passed to **FFmpeg**, placed in the video and saved

5. **Output**:
  - - A download button with the file appears and the user can then download it

## How to Use
🤳🏽
  ### 1. Building the Environment
  
  1. Open a terminal in your project folder and run the command:
  ```bash
  git clone https://github.com/rodrigoalmeida2/Legendas_Auto.git
  ```
  2. Create a virtual environment:
  ```bash
  python -m venv your_venv_name
  ```
  3. Start your venv:
  ```bash
  your_venv_name/Scripts/Activate
  ```
  4. Install FrameWorks and necessary tools:
  ```bash
  pip install -r requirements.txt
  ```
### 2. Installing FFmpeg and Configuring:

  Install Chocolatey:
  
  1. Open PowerShell as Administrator and run the following command to install Chocolatey:
```bash
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
  2. Install FFmpeg:
  1. After installing Chocolatey, run the following command in PowerShell:
  ```bash
     choco install ffmpeg
  ```
  3. After installation, you can check if FFmpeg was installed correctly:
  ```bash
  ffmpeg -version
  ```
  4. Method 2: Manual Installation:
  1. Go to [FFmpeg Manual Installation](https://youtu.be/Q267RF1I3GE)

### 3. Configure APIs
  -
  1. **Deepgram**
    1. Go to [Deepgram website](https://deepgram.com).
    2. Create an account and get your API key. 2.
  
  1. **Google Cloud**
    1. Access [Google Cloud](cloud.google.com)
    2. Create your account, access the cloud console, create a project
    3. In the project search bar, type **Cloud Translation API**
    4. When it opens, click on **enable**. The manage option will appear, click on it, then go to **Credentials**
    5. Click on **CREATE CREDENTIALS**, **API Key**

### 4. Use your keys
  - Create a ```.env``` file, paste your keys and then use dotenv to use them or put them directly in the code

### 5. Run the code
  ```bash
  streamlit run main.py
  ```
### 6. Upload Limit
  - **Streamlit** only allows 200 MB of upload. If you want to upload more than the limit, pass this command when running the code:
  ```bash
  streamlit run main.py --server.maxUploadSize 200
  ```

## Interface

![Streamlit Interface](https://github.com/user-attachments/assets/fccc882b-f43d-4e64-b6a7-e523cbc10989)


## Contribution
  🙏🏼
  Contributions are welcome! Follow the steps below:
  
  - Create a branch with your feature
  ```bash
  git checkout -b feature/new-feature
  ```
  - Commit your changes
  ```bash
  git commit -m "Add new feature"
  ```
  - Push to the original repository
  ```bash
  git push origin feature/new-feature
  ```
  - Open a Pull Request.

## Contact  
<p align="left">
  <a href="mailto:rodrigoalmeida350.ra@gmail.com" title="Gmail">
  <img src="https://img.shields.io/badge/-Gmail-FF0000?style=flat-square&labelColor=FF0000&logo=gmail&logoColor=white&link=LINK-DO-SEU-GMAIL" alt="Gmail"/></a>
  <a href="https://www.linkedin.com/in/rodrigo101/" title="LinkedIn">
  <img src="https://img.shields.io/badge/-Linkedin-0e76a8?style=flat-square&logo=Linkedin&logoColor=white&link=LINK-DO-SEU-LINKEDIN" alt="LinkedIn"/></a>
  <a href="https://www.instagram.com/rodrigoalmeida2k/" title="Instagram">
  <img src="https://img.shields.io/badge/-Instagram-DF0174?style=flat-square&labelColor=DF0174&logo=instagram&logoColor=white&link=LINK-DO-SEU-INSTAGRAM" alt="Instagram"/></a>
</p>

## License
- This project is licensed under the MIT license - see the LICENSE file for more details.

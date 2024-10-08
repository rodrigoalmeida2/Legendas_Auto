import streamlit as st
import processa_video as pv
import os
import shutil


def gerar_legenda(uploaded_file, source_lg, target_lg):
    """Processa o vídeo, gera a legenda e disponibiliza para download."""
    if uploaded_file:
        # Criar uma pasta temporária para os arquivos
        #temp_dir = "temp_folder"
        os.makedirs("temp_folder", exist_ok=True)

        # Caminho completo do arquivo de vídeo na pasta temporária
        #video_path = os.path.join("temp_folder", uploaded_file.name)

        # Salva o vídeo na pasta temporária
        with open(f"temp_folder/{uploaded_file.name}", "wb") as temp:
            temp.write(uploaded_file.getbuffer())

        # Chama a função que gera a legenda
        pv.processa_video(f"temp_folder/{uploaded_file.name}", source_lg, target_lg)

        # Gera o caminho do arquivo legendado
        subtitled_video_path = uploaded_file.name.replace(".mp4", "_subtitled.mp4")

        # Botão para download do vídeo legendado
        with open(f"temp_folder/{subtitled_video_path}", "rb") as file:
            st.download_button(
                label="Download vídeo com legenda",
                data=file,
                file_name=subtitled_video_path,
                mime="video/mp4"
            )

        # Remove a pasta temporária após o processo
        shutil.rmtree("temp_folder")

def main():
        # Título da aplicação
    st.title("Legendas Automáticas")

    # Upload do arquivo de vídeo
    uploaded_file = st.file_uploader("Escolha um arquivo de vídeo")

    # Seleção de idioma de origem
    source_lg = st.selectbox(
        "Língua de origem do vídeo:",
        ("pt", "en", "fr"),
        index=None,
        placeholder="Selecione origem..."
    )

    # Seleção de idioma para a legenda
    target_lg = st.selectbox(
        "Língua que você deseja para a legenda:",
        ("pt", "en", "fr"),
        index=None,
        placeholder="Selecione destino..."
    )

    # Botão para gerar a legenda
    if st.button("Gerar Legenda"):
        gerar_legenda(uploaded_file, source_lg, target_lg)

if __name__ == "__main__":
    main()
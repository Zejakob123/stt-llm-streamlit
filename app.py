import streamlit as st
import whisper
import tempfile
import os

def main():
    # Set the web tab name
    st.set_page_config(page_title="VTT on Whisper and Streamlit")
    st.title("Voice-to-Text Implementation by using Whisper Model and Streamlit")
    st.write("Streamlit Version: ",st.__version__)

    # Record audio from the user
    audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])
    
    # Load the Whisper model
    model = whisper.load_model("base")
    st.text("Whisper Model Loaded")

    if audio_file is not None:
        # Play the original audio file
        st.sidebar.header("Play Original Audio File")
        st.sidebar.audio(audio_file)

        # Use a temporary file to save the uploaded audio
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            temp_file.write(audio_file.read())
            temp_file_path = temp_file.name

        # Check if file was saved correctly
        if os.path.exists(temp_file_path):
            if st.sidebar.button("Transcribe Audio"):
                st.sidebar.success("Transcribing Audio")
                # Transcribe using Whisper model with the temp file path
                transcription = model.transcribe(temp_file_path, language="en")
                st.sidebar.success("Transcription Complete")
                st.markdown(transcription['text'])
        else:
            st.sidebar.error("Error saving the uploaded audio file. Please try again.")
    else:
        st.sidebar.error("Please upload an audio file")

if __name__ == "__main__":
    main()
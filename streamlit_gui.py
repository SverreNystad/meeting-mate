from time import time
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile
from recorder import DATA_FOLDER
from transcriber import Model, transcribe

st.title("Meeting Mate")
st.text("Meeting Mate is a tool for recording, transcribing, and summarizing meetings.")

# Audio input widget for recording
audio_value: UploadedFile = st.audio_input("Record the meeting")

# Sidebar for model selection
st.sidebar.title("Transcription Settings")
model_choice = st.sidebar.selectbox(
    "Choose ASR Model", list(Model), format_func=lambda m: m.value
)

if audio_value:
    st.subheader("Audio Transcription")
    st.audio(audio_value)

    # Save the recorded audio to a file
    start_time = time()
    file_name = DATA_FOLDER + f"recording_at_{int(start_time)}.wav"
    audio_value.name = file_name
    with open(file_name, "wb") as f:
        f.write(audio_value.getvalue())

    st.text("Transcription in progress...")
    transcription = transcribe(file_name, model_name=model_choice)

    st.write("### Transcription")
    st.write(transcription)

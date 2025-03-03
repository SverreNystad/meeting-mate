from time import time
import os
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile
from recorder import DATA_FOLDER
from summarizer import summarize
from transcriber import Model, transcribe

# Configure page settings
st.set_page_config(page_title="Meeting Mate", layout="wide")
st.title("Meeting Mate")
st.markdown(
    "Meeting Mate is a tool for recording, transcribing, and summarizing meetings."
)

# --- Sidebar Settings ---
st.sidebar.header("Transcription Settings")
model_choice = st.sidebar.selectbox(
    "Choose ASR Model", list(Model), format_func=lambda m: m.value
)
enable_summarization = st.sidebar.checkbox("Enable Summarization", value=True)

# --- Main Content ---
audio_value: UploadedFile = st.audio_input("Record the meeting")

if audio_value:
    st.subheader("Recorded Meeting Audio")
    st.audio(audio_value)

    # Ensure the data folder exists
    os.makedirs(DATA_FOLDER, exist_ok=True)

    # Save the recorded audio to a file with a timestamp in the name
    start_time_stamp = int(time())
    file_name = os.path.join(DATA_FOLDER, f"recording_at_{start_time_stamp}.wav")
    with open(file_name, "wb") as f:
        f.write(audio_value.getvalue())
    st.info(f"Audio saved as: **{file_name}**")

    # Transcribe the recording
    st.text("Transcription in progress...")
    with st.spinner("Transcribing audio..."):
        transcription = transcribe(file_name, model_name=model_choice)
    st.success("Transcription completed!")

    st.write("### Transcription")
    st.write(transcription)

    # Offer a download button for the transcription
    transcription_text = transcription.get("text", "")
    if transcription_text:
        st.download_button(
            label="Download Transcription",
            data=transcription_text,
            file_name="transcription.txt",
            mime="text/plain",
        )

    # Summarize the transcription if enabled
    if enable_summarization:
        if st.button("Summarize Transcription"):
            if transcription_text:
                st.text("Summarization in progress...")
                with st.spinner("Summarizing transcription..."):
                    summary = summarize(transcription_text)
                st.success("Summarization completed!")
                st.subheader("Summary")
                st.write(summary)

                if summary:
                    st.download_button(
                        label="Download summary",
                        data=summary.content,
                        file_name="summary.txt",
                        mime="text/plain",
                    )
            else:
                st.error("No transcription text available for summarization.")

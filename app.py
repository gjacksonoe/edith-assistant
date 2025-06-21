import streamlit as st
import openai

st.title("EDITH: Voice Transcription Test")

# 🔐 API key (must be in Streamlit secrets)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Upload audio
audio_file = st.file_uploader("Upload a voice recording", type=["wav", "mp3", "m4a"])

if audio_file:
    st.write("✅ File received!")
    st.audio(audio_file)

    # Transcribe using Whisper
    with st.spinner("Transcribing..."):
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        user_text = transcript["text"]

    st.write(f"🗣️ You said: `{user_text}`")
import streamlit as st
import openai
import io

st.title("EDITH: Voice Transcription Debug v3")

# Load API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Upload audio
audio_file = st.file_uploader("Upload a voice recording", type=["wav", "mp3", "m4a"])

if audio_file:
    st.write("✅ File received!")
    st.audio(audio_file)
    st.write("📡 Beginning transcription...")

    try:
        # Read audio bytes
        audio_bytes = audio_file.read()

        # Wrap in a subclassed BytesIO that forces a 'name' property
        class NamedBytesIO(io.BytesIO):
            def __init__(self, data, name):
                super().__init__(data)
                self.name = name

        audio_buffer = NamedBytesIO(audio_bytes, audio_file.name)

        st.write(f"📁 File name: {audio_file.name}")
        st.write(f"📏 File size: {len(audio_bytes)} bytes")

        with st.spinner("🔍 Transcribing your message..."):
            transcript = openai.Audio.transcribe("whisper-1", audio_buffer)
            user_text = transcript["text"]

        st.success("🧠 Transcription successful!")
        st.write(f"🗣️ You said: `{user_text}`")

    except Exception as e:
        st.error("⚠️ Transcription failed.")
        st.write("Error details:")
        st.write(str(e))
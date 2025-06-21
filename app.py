import streamlit as st
import openai
import tempfile

st.title("EDITH: Whisper Transcription – Final Fix")

# Load API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Upload audio
audio_file = st.file_uploader("Upload a voice recording", type=["wav", "mp3", "m4a"])

if audio_file:
    st.write("✅ File received!")
    st.audio(audio_file)
    st.write("📡 Saving and sending to Whisper...")

    try:
        # Save uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".m4a") as temp_audio:
            temp_audio.write(audio_file.read())
            temp_audio_path = temp_audio.name

        st.write(f"📁 Temp file path: {temp_audio_path}")

        # Send to Whisper
        with st.spinner("🔍 Transcribing your message..."):
            with open(temp_audio_path, "rb") as f:
                transcript = openai.Audio.transcribe("whisper-1", f)
                user_text = transcript["text"]

        st.success("🧠 Transcription successful!")
        st.write(f"🗣️ You said: `{user_text}`")

    except Exception as e:
        st.error("⚠️ Transcription failed.")
        st.write("Error details:")
        st.write(str(e))
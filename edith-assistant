import streamlit as st
import openai
from elevenlabs import generate, set_api_key

# Set your API keys here or use Streamlit secrets later
openai.api_key = st.secrets["OPENAI_API_KEY"]
set_api_key(st.secrets["ELEVENLABS_API_KEY"])

st.title("🕶️ EDITH - Your Jarvis Assistant")

if st.button("Start Talking"):
    audio_file = st.file_uploader("Upload a voice recording", type=["wav", "mp3"])
    if audio_file:
        # Transcribe audio using OpenAI Whisper
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        user_text = transcript['text']
        st.write(f"You said: {user_text}")

        # Chat completion with Jarvis personality
        messages = [
            {"role": "system", "content": "You are Jarvis, Tony Stark's witty British AI assistant."},
            {"role": "user", "content": user_text}
        ]
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        )
        reply_text = response.choices[0].message.content
        st.write(f"Jarvis says: {reply_text}")

        # Generate voice from ElevenLabs and play audio
        audio = generate(text=reply_text, voice="21m00Tcm4TlvDq8ikWAM", model="eleven_multilingual_v1")
        st.audio(audio)

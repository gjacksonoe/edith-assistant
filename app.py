import streamlit as st

st.title("EDITH: Voice Assistant Test")

audio_file = st.file_uploader("Upload a voice recording", type=["wav", "mp3", "m4a"])

if audio_file:
    st.write("✅ File received!")
    st.audio(audio_file)
    st.write("This is just a test to make sure file uploading works.")
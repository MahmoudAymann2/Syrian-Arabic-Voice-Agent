import streamlit as st
from agent import handle_user_input
import os

st.title("🧪 Charco Chicken Voice Agent")
audio_file = st.file_uploader("ارفع ملف صوتي عربي", type=["wav", "mp3"])

if audio_file:
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_file.read())
    st.audio("temp_audio.wav")

    text, intent, response_text, audio_path = handle_user_input("temp_audio.wav")

    st.write(f"📝 التفريغ: {text}")
    st.write(f"🎯 النية: {intent}")
    st.write(f"🤖 الرد: {response_text}")
    st.audio(audio_path)
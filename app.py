import streamlit as st
import whisper
from pytube import YouTube
import os
import uuid
import shutil

# Load Whisper model once
@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

# Download audio from a public YouTube video
def download_audio(url):
    video = YouTube(url)
    audio_stream = video.streams.filter(only_audio=True).first()
    unique_name = f"audio_{uuid.uuid4().hex}.mp4"
    audio_path = audio_stream.download(filename=unique_name)
    return audio_path

# Transcribe with Whisper
def transcribe(audio_path):
    result = model.transcribe(audio_path)
    text = result['text']
    lang = result['language']
    return text, lang

# Heuristic-based accent detection
def analyze_accent(text):
    if any(word in text.lower() for word in ["gonna", "gotta", "wanna", "dude", "kinda"]):
        return "American", 85
    elif any(word in text.lower() for word in ["mate", "bloody", "flat", "trousers"]):
        return "British", 80
    elif any(word in text.lower() for word in ["reckon", "heaps", "brekkie"]):
        return "Australian", 75
    else:
        return "English (Unclear origin)", 60

# Streamlit UI
st.title("🎙️ English Accent Detector")
st.write("Enter a public video URL (e.g., YouTube, Loom, etc.)")

video_url = st.text_input("Video URL")

if st.button("Analyze") and video_url:
    try:
        st.info("🔄 Downloading and processing video...")
        audio_file = download_audio(video_url)

        st.info("🧠 Transcribing with Whisper...")
        text, language = transcribe(audio_file)

        st.info("🔍 Detecting accent...")
        accent, confidence = analyze_accent(text)

        st.success("✅ Analysis complete!")
        st.markdown(f"**Detected Accent:** `{accent}`")
        st.markdown(f"**English Accent Confidence:** `{confidence}%`")
        st.markdown("**Transcript:**")
        st.text_area("Speech Text", text, height=200)

        os.remove(audio_file)
    except Exception as e:
        st.error(f"An error occurred: {e}")

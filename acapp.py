import streamlit as st
import whisper
import yt_dlp
import os
import uuid
import glob


# Load Whisper model once
@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

# Download audio using yt_dlp

def download_audio(url):
    base_name = f"audio_{uuid.uuid4().hex}"
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': base_name,  # No extension here
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'noplaylist': True
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # Find the actual .mp3 file using glob
        audio_files = glob.glob(f"{base_name}*.mp3")
        if not audio_files:
            raise Exception("Audio file not found after download.")

        return audio_files[0]
    except Exception as e:
        raise Exception(f"Failed to download audio: {e}")



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
st.write("Enter a public YouTube video URL")

video_url = st.text_input("YouTube Video URL")

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

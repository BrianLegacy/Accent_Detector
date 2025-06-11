# 🎙️ English Accent Detector

A simple Streamlit app that detects English accents from public YouTube videos using OpenAI's Whisper model.

---

## 🔧 Features

- 📥 Download audio from YouTube videos
- 🧠 Transcribe speech using Whisper
- 🌍 Detect English accents (American, British, Australian)
- 📃 Display transcript and confidence score

---

## 🚀 Getting Started

### 1. Clone the Repository


git clone https://github.com/yourusername/english-accent-detector.git
cd english-accent-detector
2. Install Dependencies
Make sure you have Python 3.8+ and ffmpeg installed.


pip install -r requirements.txt
3. Install ffmpeg
On Ubuntu/Debian:

bash
sudo apt update && sudo apt install ffmpeg
On Windows:

Download ffmpeg from ffmpeg.org/download

Extract the files

Add the bin/ folder to your system PATH

4. Run the App
bash
streamlit run app.py
📦 Requirements
streamlit

yt_dlp

openai-whisper

ffmpeg (must be installed separately)

Install Python dependencies using:


pip install streamlit yt_dlp git+https://github.com/openai/whisper.git
🧠 How it Works
User pastes a public YouTube URL

The app downloads and extracts the audio as MP3 using yt_dlp and ffmpeg

Whisper transcribes the spoken words into text

A basic heuristic is used to detect likely English accent origin based on word patterns

📝 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Brian Munene Muriuki
📧 muriuki.brian@outlook.com
🇰🇪 Kenya


This version:
- Properly formats all code blocks with triple backticks
- Maintains consistent heading levels
- Includes proper Markdown syntax for links and images
- Organizes sections clearly with dividers
- Preserves all emojis and formatting


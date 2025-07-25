import speech_recognition as sr
import subprocess
import os
import yt_dlp
import shutil


# 1️⃣ Ensure FFmpeg is Installed
def check_ffmpeg():
    if not shutil.which("ffmpeg"):
        raise RuntimeError("FFmpeg is not installed or not in the system PATH.")


# 2️⃣ Download YouTube Video and Extract Audio
def download_youtube_audio(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'video_audio.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return os.path.abspath("video_audio.mp3")
    except Exception as e:
        raise RuntimeError(f"Error downloading video: {e}")


# 3️⃣ Convert Audio to WAV (for better recognition)
def convert_audio_to_wav(audio_path):
    check_ffmpeg()
    wav_path = "audio.wav"
    command = ["ffmpeg", "-i", audio_path, "-ac", "1", "-ar", "16000", "-y", wav_path]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return wav_path


# 4️⃣ Speech Recognition
def speech_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Speech not recognized"
        except sr.RequestError as e:
            return f"Speech recognition error: {e}"


# 5️⃣ Map Text to ISL Animation
def display_sign_animation(isl_animation_path):
    print(f"Displaying ISL animation: {isl_animation_path}")
    os.system(f"start {isl_animation_path}")  # Open the animation file


# 🔹 Main Execution
def main():
    video_link = input("Paste the video link: ")  # User pastes YouTube video link
    audio_path = download_youtube_audio(video_link)
    wav_audio = convert_audio_to_wav(audio_path)

    detected_text = speech_to_text(wav_audio)
    print(f"Extracted Speech: {detected_text}")

    isl_path = r'C:\Users\Admin\Documents\SWATHI\LLM' # You provide ISL animation path
    display_sign_animation(isl_path)


if __name__ == "__main__":
    main()

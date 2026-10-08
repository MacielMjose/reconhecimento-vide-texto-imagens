try:
    import moviepy as moviepy  # type: ignore[reportMissingImports]
except ImportError as exc:
    raise RuntimeError(
        "A biblioteca moviepy não está instalada. Instale com: pip install moviepy"
    ) from exc
import speech_recognition as sr
import os


def extract_audio_from_video(video_path, audio_path):
    video = moviepy.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

def transcrive_audio_to_text(audio_path, text_output_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        text= recognizer.recognize_google(audio, language="pt-BR")
        print("Transcrição", text)

        with open(text_output_path, "w", encoding = "utf-8" ) as file:
            file.write(text)
    
    except sr.UnknownValueError:
        print("O Google Speech Recognition Não conseguiu entender o áudio")
    except sr.RequestError as e:
        print(f"Erro ao solicitar serviços de reconhecimento de fala do google: {e}")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    video_path = os.path.join(script_dir, "video.mp4")
    audio_path = os.path.join(script_dir, "audio.wav")
    text_output_path = os.path.join(script_dir, "transcription.txt")

    extract_audio_from_video(video_path, audio_path)
    transcrive_audio_to_text(audio_path, text_output_path)

import openai

def transcribe_audio(audio_file_path):
    with open(audio_file_path, "rb") as file:
        transcription = openai.Audio.transcribe("whisper-1", file)
    return transcription.text

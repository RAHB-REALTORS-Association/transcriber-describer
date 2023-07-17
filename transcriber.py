import openai

def transcribe_audio(audio_file_path):
    file = open(audio_file_path, "rb")
    transcription = openai.Audio.transcribe("whisper-1", file)
    return transcription.text

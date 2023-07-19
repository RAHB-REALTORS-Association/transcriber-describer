import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

def extract_audio_from_video(video_file_path, audio_file_path):
    video_clip = VideoFileClip(video_file_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile("temp.wav")
    
    # Convert WAV to MP3
    sound = AudioSegment.from_wav("temp.wav")
    sound.export(audio_file_path, format="mp3", bitrate="64k")

    # Remove temporary WAV file
    os.remove("temp.wav")
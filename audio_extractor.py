import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

def extract_audio_from_video(video_file_path, audio_file_path, time=None, bitrate=None):
    video_clip = VideoFileClip(video_file_path)
    
    if time is not None:
        video_clip = video_clip.subclip(0, time)  # extract the subclip between 0 and time seconds

    audio_clip = video_clip.audio
    audio_clip.write_audiofile("temp.wav")
    
    # Convert WAV to MP3
    sound = AudioSegment.from_wav("temp.wav")
    
    # If bitrate is specified, format it as a string for pydub
    if bitrate is not None:
        bitrate = f"{bitrate}k"
    
    sound.export(audio_file_path, format="mp3", bitrate=bitrate)

    # Remove temporary WAV file
    os.remove("temp.wav")

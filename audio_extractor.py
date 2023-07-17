from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_file_path, audio_file_path):
    video_clip = VideoFileClip(video_file_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_file_path)

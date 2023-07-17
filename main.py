import os
from transcriber import transcribe_audio
from describer import generate_description
from audio_extractor import extract_audio_from_video

def process_video_files(video_files_directory):
    video_files = os.listdir(video_files_directory)

    for video_file in video_files:
        if not (video_file.endswith(".mp4") or video_file.endswith(".avi") or video_file.endswith(".mov")):
            continue

        video_file_path = os.path.join(video_files_directory, video_file)
        audio_file_path = video_file_path + ".wav"
        extract_audio_from_video(video_file_path, audio_file_path)
        transcription = transcribe_audio(audio_file_path)
        description = generate_description(transcription)
        print(f'Description for {video_file}: {description}')
        os.remove(audio_file_path)

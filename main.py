import os
import argparse
from transcriber import transcribe_audio
from describer import generate_description
from audio_extractor import extract_audio_from_video

def process_video_files(video_files_directory):
    video_files = os.listdir(video_files_directory)

    for video_file in video_files:
        if not (video_file.endswith(".mp4") or video_file.endswith(".avi") or video_file.endswith(".mov")):
            continue

        # Remove file extension from video_file to generate original file name
        original_file_name, _ = os.path.splitext(video_file)

        video_file_path = os.path.join(video_files_directory, video_file)
        audio_file_path = os.path.join(video_files_directory, f"{original_file_name}_audio.mp3")
        transcript_file_path = os.path.join(video_files_directory, f"{original_file_name}_transcript.txt")
        description_file_path = os.path.join(video_files_directory, f"{original_file_name}_description.txt")

        extract_audio_from_video(video_file_path, audio_file_path)
        
        transcription = transcribe_audio(audio_file_path)

        # Save the transcription into a .txt file
        with open(transcript_file_path, 'w') as f:
            f.write(transcription)

        description = generate_description(transcription)

        # Save the description into a .txt file
        with open(description_file_path, 'w') as f:
            f.write(description)

        print(f'Description for {video_file}: {description}')
        os.remove(audio_file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process video files in a directory.')
    parser.add_argument('directory', type=str, help='The directory containing video files.')
    args = parser.parse_args()
    process_video_files(args.directory)

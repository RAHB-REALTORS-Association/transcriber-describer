import os
import argparse
from audio_extractor import extract_audio_from_video
from transcriber import transcribe_audio,transcribe_audio_local
from describer import generate_description,generate_description_local

def process_video_files(args):
    video_files_directory = args.directory
    video_files = os.listdir(video_files_directory)

    for video_file in video_files:
        if not (video_file.endswith(".mp4") or video_file.endswith(".avi") or video_file.endswith(".mov")):
            continue

        # Remove file extension from video_file to generate original file name
        original_file_name, _ = os.path.splitext(video_file)

        video_file_path = os.path.join(video_files_directory, video_file)
        audio_file_path = os.path.join(video_files_directory, f"{original_file_name}_audio.mp3")
        transcript_file_path = os.path.join(video_files_directory, f"{original_file_name}_transcript.srt")
        description_file_path = os.path.join(video_files_directory, f"{original_file_name}_description.txt")

        extract_audio_from_video(video_file_path, audio_file_path)

        if args.local or args.local_transcribe:
            transcription = transcribe_audio_local(audio_file_path)
        else:
            transcription = transcribe_audio(audio_file_path)

        # Save the transcription into a .srt file
        transcription.save(transcript_file_path)

        # Convert the transcription into plain text for description generation
        transcription_text = "\n".join([subtitle.text for subtitle in transcription])

        if args.local or args.local_describe:
            description = generate_description_local(transcription_text)
        else:
            description = generate_description(transcription_text)

        # Save the description into a .txt file
        with open(description_file_path, 'w') as f:
            f.write(description)

        print(f'Description for {video_file}: {description}')
        os.remove(audio_file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process video files in a directory.')
    parser.add_argument('directory', type=str, help='The directory containing video files.')
    parser.add_argument('--local', action='store_true', help='Use local versions of both transcribe and describe functions.')
    parser.add_argument('--local-transcribe', action='store_true', help='Use local version of transcribe function.')
    parser.add_argument('--local-describe', action='store_true', help='Use local version of describe function.')
    args = parser.parse_args()
    process_video_files(args)

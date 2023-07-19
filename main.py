import os
import argparse
from audio_extractor import extract_audio_from_video
from transcriber import transcribe_audio, transcribe_audio_local
from describer import generate_description, generate_description_local
from translator import translate_subtitle
import re

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
        
        transcript_file_path = ""
        if args.local or args.local_transcribe:
            transcript_file_path = os.path.join(video_files_directory, f"{original_file_name}_transcript.srt")
        else:
            transcript_file_path = os.path.join(video_files_directory, f"{original_file_name}_transcript.txt")

        description_file_path = os.path.join(video_files_directory, f"{original_file_name}_description.txt")

        # Check if files already exist and whether we should overwrite
        if not args.overwrite and (os.path.exists(audio_file_path) or os.path.exists(transcript_file_path) or os.path.exists(description_file_path)):
            print(f'Skipping {video_file} as output files already exist')
            continue

        extract_audio_from_video(video_file_path, audio_file_path, args.time, args.bitrate)

        if args.local or args.local_transcribe:
            transcription = transcribe_audio_local(audio_file_path)
            if args.translate:
                orig_language, translation_language = args.translate.split(":")
                transcription = translate_subtitle(transcription, orig_language, translation_language)
            # Save the transcription into a .srt file
            transcription.save(transcript_file_path)
            if not args.keep_transcripts:
                os.remove(transcript_file_path)
            # Convert the transcription into plain text for description generation
            transcription_text = "\\n".join([subtitle.text for subtitle in transcription])
        else:
            transcription_text = transcribe_audio(audio_file_path)
            if args.translate:
                orig_language, translation_language = args.translate.split(":")
                transcription_text = translate_subtitle(transcription_text, orig_language, translation_language)
            # Save the transcription into a .txt file
            with open(transcript_file_path, 'w') as f:
                f.write(transcription_text)
            if not args.keep_transcripts:
                os.remove(transcript_file_path)

        if args.local or args.local_describe:
            description = generate_description_local(transcription_text, args.model)
        else:
            description = generate_description(transcription_text, args.model)

        # Save the description into a .txt file
        with open(description_file_path, 'w') as f:
            f.write(description)

        print(f'Description for {video_file}: {description}')
        if not args.keep_audio:
            os.remove(audio_file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process video files in a directory.')
    parser.add_argument('directory', type=str, help='The directory containing video files.')
    parser.add_argument('--model', type=str, default='gpt-3.5-turbo', help='Model name to use for description generation.')
    parser.add_argument('--local', action='store_true', help='Use local versions of both transcribe and describe functions.')
    parser.add_argument('--local-transcribe', action='store_true', help='Use local version of transcribe function.')
    parser.add_argument('--local-describe', action='store_true', help='Use local version of describe function.')
    parser.add_argument('--time', type=int, help='Duration in seconds of the video to transcribe.')
    parser.add_argument('--bitrate', type=int, help='Bitrate for the extracted audio.')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite existing audio, transcript, and description files.')
    parser.add_argument('--translate', type=str, help='Translation in the form <orig_language>:<translation_language>.')
    parser.add_argument('--keep-transcripts', action='store_true', help='Keep generated transcript files.')
    parser.add_argument('--keep-audio', action='store_true', help='Keep extracted audio files.')
    args = parser.parse_args()
    process_video_files(args)

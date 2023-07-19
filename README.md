# Transcriber-Describer

This project transcribes audio from video files and generates descriptions from the transcriptions. It uses OpenAI's **Whisper API** for transcription and the **ChatGPT-3.5-turbo** model for generating descriptions. The user can opt to use a local model for both tasks if desired. The tool also supports extracting a specific duration from the start of the video and controlling the bitrate of the audio.

### How to Run
You can run the main Python script from the terminal with several optional flags:

```bash
python main.py /path/to/video/folder --local --local-transcribe --local-describe --time <seconds> --bitrate <bitrate> --overwrite
```

- The `--local` flag uses local versions of both the transcribe and describe functions.
- The `--local-transcribe` flag uses the local version of the transcribe function.
- The `--local-describe` flag uses the local version of the describe function.
- The `--time` flag sets the duration in seconds of the video to transcribe.
- The `--bitrate` flag sets the bitrate for the extracted audio.
- The `--overwrite` flag enables overwriting of existing audio, transcript, or description files.

If you just want to process the video files in a directory without using any flags, you can do so:

```bash
python main.py /path/to/video/folder
```

### Setting up your OpenAI API credentials:

1. Sign up for an OpenAI account if you don't already have one.
2. Navigate to the API section of the OpenAI Dashboard.
3. Generate a new API key by clicking the "Create API Key" button.
4. Securely store your API Key.
5. Set your API Key as an environment variable in your system: `export OPENAI_API_KEY="your-api-key"`.

### Installing Dependencies
This project uses the `openai`, `moviepy`, `pydub`, and `pysubs2` libraries. You can install them using pip:

```bash
pip install openai moviepy pydub pysubs2
```
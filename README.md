# Transcriber-Describer

This project transcribes audio from video files and generates descriptions from the transcriptions. It uses OpenAI's Whisper API for transcription and the ChatGPT-3.5-turbo model for generating descriptions.

### How to Run
You can run the main Python script from the terminal:

```bash
python main.py
```

### Setting up your OpenAI API credentials:

1. Sign up for an OpenAI account if you don't already have one.
2. Navigate to the API section of the OpenAI Dashboard.
3. Generate a new API key by clicking the "Create API Key" button.
4. Securely store your API Key.
5. Set your API Key as an environment variable in your system: `export OPENAI_API_KEY="your-api-key"`.

### Installing Dependencies
This project uses the openai and moviepy libraries. You can install them using pip:

```bash
pip install openai moviepy
```
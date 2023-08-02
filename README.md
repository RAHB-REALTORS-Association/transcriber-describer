# 🗣 Transcriber-Describer 📝

[![Continuous Integration](https://github.com/RAHB-REALTORS-Association/transcriber-describer/actions/workflows/python-app.yml/badge.svg)](https://github.com/RAHB-REALTORS-Association/transcriber-describer/actions/workflows/python-app.yml)
[![Docker Image](https://github.com/RAHB-REALTORS-Association/transcriber-describer/actions/workflows/docker-image.yml/badge.svg)](https://github.com/RAHB-REALTORS-Association/transcriber-describer/actions/workflows/docker-image.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project transcribes audio from video files and generates descriptions from the transcriptions. It uses OpenAI's **Whisper API** for transcription and the **ChatGPT-3.5-turbo** model for generating descriptions. The user can opt to use a local model for both tasks if desired. The tool also supports extracting a specific duration from the start of the video and controlling the bitrate of the audio.

## Table of Contents
- [🧑‍💻 How to Run](#-how-to-run)
- [🔑 Setting up your OpenAI API credentials](#-setting-up-your-openai-api-credentials)
- [📦 Installing Dependencies](#-installing-dependencies)
- [🐳 Running with Docker](#-running-with-docker)
- [🌐 Community](#-community)
  - [Contributing 👥🤝](#contributing-)
  - [Reporting Bugs 🐛📝](#reporting-bugs-)
- [📄 License](#-license)

## 🧑‍💻 How to Run

You can run the main Python script from the terminal with several optional flags:

```bash
python main.py /path/to/video/folder --local --local-transcribe --local-describe --time <seconds> --bitrate <bitrate> --overwrite
```

- The `--model` flag sets the OpenAI model to use for description generation. The default is gpt-3.5-turbo.
- The `--local` flag uses local versions of both the transcribe and describe functions.
- The `--local-transcribe` flag uses the local version of the transcribe function.
- The `--local-describe` flag uses the local version of the describe function.
- The `--time` flag sets the duration in seconds of the video to transcribe.
- The `--bitrate` flag sets the bitrate for the extracted audio.
- The `--overwrite` flag enables overwriting of existing audio, transcript, or description files.
- The `--translate` flag is used for translating the transcription. It should be in the format <orig_language>:<translation_language>.
- The `--keep-transcripts` flag, if set, allows you to keep the generated transcript files after the program has run.
- The `--keep-audio` flag, if set, allows you to keep the extracted audio files after the program has run.

If you just want to process the video files in a directory without using any flags, you can do so:

```bash
python main.py /path/to/video/folder
```

## 🔑 Setting up your OpenAI API credentials

1. Sign up for an OpenAI account if you don't already have one.
2. Navigate to the API section of the OpenAI Dashboard.
3. Generate a new API key by clicking the "Create API Key" button.
4. Securely store your API Key.
5. Set your API Key as an environment variable in your system: `export OPENAI_API_KEY="your-api-key"`.

## 📦 Installing Dependencies

This project uses the `ffmpeg` library from your operating system, the `git` utility is also required to install SubsAI for local transcription. You can install them with your package manager, for example on Ubuntu/Debian:

```bash
sudo apt-get install ffmpeg git
```

This project uses the `openai`, `moviepy`, and `pydub` Python libraries. You can install them using pip:

```bash
pip install openai moviepy pydub
```

For local transcription, the SubsAI Python project is used, you can install it from GitHub:

```bash
pip install git+https://github.com/abdeladim-s/subsai.git
```

For local description, any app or library that provides an OpenAI-compatible API can be used, such as [LM Studio](https://lmstudio.ai).

## 🐳 Running with Docker

To get started, you first need to pull the Docker image from the GitHub Container Registry. You can do this by running the following command in your terminal:

```sh
docker pull ghcr.io/rahb-realtors-association/transcriber-describer:latest
```

Run with the following command:

```sh
docker run -it ghcr.io/rahb-realtors-association/transcriber-describer:latest <flags>
```

## 🌐 Community

### Contributing 👥🤝

Contributions of any kind are very welcome, and would be much appreciated. For Code of Conduct, see [Contributor Convent](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

To get started, fork the repo, make your changes, add, commit and push the code, then come back here to open a pull request. If you're new to GitHub or open source, [this guide](https://www.freecodecamp.org/news/how-to-make-your-first-pull-request-on-github-3#let-s-make-our-first-pull-request-) or the [git docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) may help you get started, but feel free to reach out if you need any support.

[![Submit a
PR](https://img.shields.io/badge/Submit_a_PR-GitHub-%23060606?style=for-the-badge&logo=github&logoColor=fff)](https://github.com/RAHB-REALTORS-Association/transcriber-describer/compare)

### Reporting Bugs 🐛📝

If you've found something that doesn't work as it should, or would like to suggest a new feature, then go ahead and raise an issue on GitHub. For bugs, please outline the steps needed to reproduce, and include relevant info like system info and resulting logs.

[![Raise an
Issue](https://img.shields.io/badge/Raise_an_Issue-GitHub-%23060606?style=for-the-badge&logo=github&logoColor=fff)](https://github.com/RAHB-REALTORS-Association/transcriber-describer/issues/new/choose)

## 📄 License
This project is open sourced under the MIT license. See the [LICENSE](LICENSE) file for more info. 📜

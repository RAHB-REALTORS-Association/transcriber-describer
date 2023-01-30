const fs = require('fs');
const path = require('path');
const util = require('util');
const exec = util.promisify(require('child_process').exec);
const speech = require('@google-cloud/speech');
const client = new speech.SpeechClient();
const request = {
  config: {
    encoding: 'LINEAR16',
    sampleRateHertz: 44100,
    languageCode: 'en-US',
  },
};
const openai = require('openai');
openai.apiKey = "YOUR_API_KEY";

async function transcribeAudio(filename) {
  const audioBytes = fs.readFileSync(filename);

  request.audio = {
    content: audioBytes.toString('base64'),
  };

  const [response] = await client.recognize(request);
  const transcript = response.results
    .map(result => result.alternatives[0].transcript)
    .join('\n');

  return transcript;
}

async function summarizeTranscript(transcription) {
  const prompt = `Please summarize the following text: ${transcription}`;

  openai.Completion.create({
    prompt: prompt,
    engine: "text-davinci-002"
  }).then(completion => {
    console.log(completion.choices[0].text);
    // do something with the summary
    return completion.choices[0].text;
  });
}

async function generateSubtitles(transcript) {
  const lines = transcript.split("\n");

  let srt = "";
  let counter = 1;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    // start time and end time can be set as desired
    srt += `${counter}\n00:00:00,000 --> 00:00:05,000\n${line}\n\n`;
    counter++;
  }

  fs.writeFileSync("subtitles.srt", srt);
  console.log("Subtitle file generated!");
}

async function processVideo(videoPath) {
  const { name, ext } = path.parse(videoPath);
  const audioPath = `${name}.wav`;

  console.log(`Extracting audio track from ${videoPath}`);
  const { stdout, stderr } = await exec(`ffmpeg -i "${videoPath}" -acodec pcm_s16le -ac 1 -ar 44100 "${audioPath}"`);
  console.log(stdout);
  console.error(stderr);

  console.log(`Transcribing audio from ${audioPath}`);
  const transcript = await transcribeAudio(audioPath);
  console.log(`Transcript: ${transcript}`);

  console.log(`Summarizing transcript`);
  const summary = await summarizeTranscript(transcript);
  console.log(`Summary: ${summary}`);

  console.log(`Generating subtitles`);
  await generateSubtitles(transcript);
}

async function main(directory) {
  const files = fs.readdirSync(directory);
  const videos = files.filter(file => path.extname(file) === '.mp4');

  for (const video of videos) {
    const videoPath = path.join(directory, video);
    console.log(`Processing ${videoPath}`);
    await processVideo(videoPath);
    console.log("");
  }
  
  console.log("All videos processed!");
}
    
const directory = process.argv[2];
if (!directory) {
  console.error("No directory provided. Usage: node index.js <directory>");
  process.exit(1);
}
    
main(directory).catch(error => {
  console.error(error);
  process.exit(1);
});
import openai

def generate_description(transcription):
    prompt = f"I have a transcript of an audio file and I need a brief description or summary of it. Here's the transcript followed by ENDOFTRANSCRIPT: \"{transcription}\" ENDOFTRANSCRIPT. Can you provide a summary?"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes and describes audio transcripts with no other commentary so that they can be copied into a video description."},
            {"role": "user", "content": prompt}
        ]
    )

    description = completion['choices'][0]['message']['content']
    return description

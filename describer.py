import openai

def generate_description(transcription):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": transcription}]
    )
    description = completion['choices'][0]['message']['content']
    return description

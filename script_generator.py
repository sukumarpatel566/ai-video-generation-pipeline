import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_script(topic):
    prompt = f"Write a 1 minute YouTube video script about {topic}. Simple English, engaging narration."

    chat = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
    )

    return chat.choices[0].message.content


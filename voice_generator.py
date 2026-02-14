import os
import asyncio
import edge_tts

async def text_to_speech(text):
    # 🔥 create output folder automatically
    os.makedirs("output", exist_ok=True)

    communicate = edge_tts.Communicate(text, voice="en-US-AriaNeural")
    await communicate.save("output/voice.mp3")

def generate_voice(script):
    asyncio.run(text_to_speech(script))



import edge_tts, asyncio

async def text_to_speech(text, output="output/voice.mp3"):
    communicate = edge_tts.Communicate(text, "en-US-GuyNeural")
    await communicate.save(output)

def generate_voice(script):
    asyncio.run(text_to_speech(script))

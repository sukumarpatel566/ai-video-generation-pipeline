
from script_generator import generate_script
from voice_generator import generate_voice
from video_fetcher import fetch_videos
from video_editor import create_final_video

topic = input("Enter video topic: ")

print("Generating script...")
script = generate_script(topic)

print("Generating voice...")
generate_voice(script)

print("Fetching videos...")
videos = fetch_videos(topic)

print("Creating final video...")
create_final_video(videos)

print("VIDEO CREATED: output/final_video.mp4")

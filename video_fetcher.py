
import requests, os
from dotenv import load_dotenv

load_dotenv()
PEXELS_KEY = os.getenv("PEXELS_API_KEY")

def fetch_videos(topic):
    url = f"https://api.pexels.com/videos/search?query={topic}&per_page=3"
    headers = {"Authorization": PEXELS_KEY}
    r = requests.get(url, headers=headers).json()
    videos = []
    for i, vid in enumerate(r["videos"]):
        video_url = vid["video_files"][0]["link"]
        video_data = requests.get(video_url).content
        path = f"assets/video{i}.mp4"
        open(path, "wb").write(video_data)
        videos.append(path)
    return videos

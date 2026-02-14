import os
import requests

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def fetch_videos(topic):
    print("Fetching videos from Pexels...")
    url = f"https://api.pexels.com/videos/search?query={topic}&per_page=3"

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        # If API fails → fallback
        if response.status_code != 200:
            raise Exception("Pexels API failed")

        data = response.json()
        videos = []

        for i, vid in enumerate(data["videos"]):
            video_url = vid["video_files"][0]["link"]
            video_data = requests.get(video_url).content
            path = f"assets/video{i}.mp4"
            open(path, "wb").write(video_data)
            videos.append(path)

        print("Videos downloaded successfully!")
        return videos

    except Exception as e:
        print("⚠️ Pexels failed. Using fallback video.")
        return ["fallback.mp4"]

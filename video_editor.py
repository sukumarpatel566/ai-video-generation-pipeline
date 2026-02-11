from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips

def create_final_video(video_files):
    clips = [VideoFileClip(v).subclipped(0,5) for v in video_files]
    final = concatenate_videoclips(clips)

    audio = AudioFileClip("output/voice.mp3")
    final = final.with_audio(audio)

    final.write_videofile("output/final_video.mp4", fps=24)


from moviepy import VideoFileClip

def create_thumbnail():
    # load final video
    clip = VideoFileClip("output/final_video.mp4")

    # take frame at 1 second
    frame = clip.get_frame(1)

    # save thumbnail
    from PIL import Image
    img = Image.fromarray(frame)
    img.save("output/thumbnail.png")

    print("Thumbnail created!")

if __name__ == "__main__":
    create_thumbnail()


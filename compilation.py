from os import listdir
from os.path import isfile, join
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Specify the folder path
folder = "C://Users//amaha//VS_Python_Projects//discord_image_bot//test_videos"

# Get all the files in the folder
files = listdir(folder)

# Filter only the mp4 files
webm_files = [f for f in files if f.endswith(".webm")]

# Create a list of clips
clips = []
for file in webm_files:
    # Create a VideoFileClip object for each file
    clip = VideoFileClip(join(folder, file))
    # Append the clip to the list
    clips.append(clip)

# Concatenate all the clips
final_clip = concatenate_videoclips(clips)

# Write the output video file
final_clip.write_videofile("final_video.webm", fps=30)

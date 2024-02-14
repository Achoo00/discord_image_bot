# Finished
# Downloads youtube videos from a filtered out txt file of the DMs
from yt_dlp import YoutubeDL
from pytube import YouTube # Need to use pytube for video length because yt_dlp doesnt do that anymore
import os

ydl_opts = {
    'format': 'bestvideo[height<=360]+bestaudio/best[height<=360]', # Select the best quality video that is 360p or lower
    'outtmpl': '%(title)s.%(ext)s', # Use the video title as the output filename
}

def download():
    ydl = YoutubeDL(ydl_opts)
    os.chdir("C://Users//amaha//VS_Python_Projects//discord_image_bot//videos")
    video_url = input("Insert video url here:" + "")
    try:
        ydl.download(video_url)
    except Exception as e: # Will skip url if any exception happens
        print(f"Could not download {video_url}")

download()
os.startfile('C:\\Users\\amaha\\VS_Python_Projects\\discord_image_bot\\videos')
# Finished
# Downloads youtube videos from a filtered out txt file of the DMs
from yt_dlp import YoutubeDL
from pytube import YouTube # Need to use pytube for video length because yt_dlp doesnt do that anymore
import os

ydl_opts = {
    'format': 'bestvideo[height<=360]+bestaudio/best[height<=360]', # Select the best quality video that is 360p or lower
    'outtmpl': '%(title)s.%(ext)s', # Use the video title as the output filename
}

def download(URLS):
    ydl = YoutubeDL(ydl_opts)
    os.chdir("C://Users//amaha//VS_Python_Projects//discord_image_bot//videos")
    for url in URLS:
        try:
            new_url = url.replace("'",'')
            yt = YouTube(new_url)
            # Get the duration of the video in seconds
            video_length = yt.length
            #print("length of video", video_length)
            # Check if the duration is longer than 10 minutes
            if video_length < 600:
                ydl.download(new_url)
        except Exception as e: # Will skip url if any exception happens
            print(f"Could not download {new_url}")

f = open('Filtered_DMs.txt','r', encoding='utf8') # utf8 encoding because of a UnicodeDecodeError
data = f.read()
data_split = data.split(',')
download(data_split)

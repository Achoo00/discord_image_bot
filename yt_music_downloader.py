# Finished
# Downloads youtube video playlist as audio
from pytube import Playlist # Need to use pytube for video length because yt_dlp doesnt do that anymore
import os
from tqdm import tqdm

def download():
    os.chdir("C://Users//amaha//VS_Python_Projects//discord_image_bot//music")
    p = Playlist("https://www.youtube.com/playlist?list=PLxx8aBNNbWW5GgAX6fRSAPt8M6JgfK0i6")
    for audio in tqdm(p.videos):
        try:
            audio_stream = audio.streams.filter(only_audio=True).first()
            audio_stream.download()
        except Exception as e:
            print(f"Could not download {audio}")
            #print(Exception)

download()

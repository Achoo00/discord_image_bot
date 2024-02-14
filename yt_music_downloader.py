# Finished
# Downloads youtube video playlist or individual video as audio
from pytube import Playlist, YouTube # Need to use pytube for video length because yt_dlp doesnt do that anymore
import os
from tqdm import tqdm

def download_individual():
    os.chdir("C://Users//amaha//VS_Python_Projects//discord_image_bot//music")
    playlist_url = input("Insert youtube video here:" + "")
    yt = YouTube(playlist_url)
    try:
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download()
        print(f"Sucessfully downloaded {playlist_url}")
    except Exception as e:
        print(f"Could not download {playlist_url}")
        #print(Exception)


def download_playlist():
    os.chdir("C://Users//amaha//VS_Python_Projects//discord_image_bot//music")
    playlist_url = input("Insert youtube playlist here:" + "")
    p = Playlist(playlist_url)
    for audio in tqdm(p.videos):
        try:
            audio_stream = audio.streams.filter(only_audio=True).first()
            audio_stream.download()
        except Exception as e:
            print(f"Could not download {audio}")
            #print(Exception)


individual_or_playlist = input("Individual Video [1] or Playlist [2]:" + "")
if int(individual_or_playlist) == 1:
    download_individual()
elif int(individual_or_playlist) == 2:
    download_playlist()

os.startfile('C:\\Users\\amaha\\VS_Python_Projects\\discord_image_bot\\music')

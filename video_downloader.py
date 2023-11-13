from yt_dlp import YoutubeDL
import re
from pytube import YouTube # Need to use pytube for video length because yt_dlp doesnt do that anymore
import os
#Stuff to do
#1. UnicodeDecodeError txt file has weird characters in it,find some way of deleting it or change encoding - done
#2. Anything longer than 10 minutes is skipped ex: 7h livestream 'https://www.youtube.com/watch?v=Hko7bqYiJow (private)' - done


#Types of urls
#https://www.youtube.com/watch?v=Vr54kmrnCFU
#https://youtu.be/Ks2UnT4Nzcs
#https://youtube.com/playlist?list=PLZ34fLWik_iASrR26p_41rirqp8GkPAr_

#Youtube urls will always have 11 characters after "watch?v=" or after "be/" or after "shorts/"

# Stuff to read on
#https://www.w3schools.com/python/ref_string_rsplit.asp
#https://codefather.tech/blog/python-check-for-duplicates-in-list/?expand_article=1

#URLS = ['https://www.youtube.com/PointCrow','https://www.youtube.com/watch?v=BaW_jenozKc',"https://www.youtube.com/watch?v=3m7ZUL8zJSc"]

def download(URLS):
    #URLS = ['https','https://www.youtube.com/...','https://www.youtube.com/watch?v=cdkPHgbE...','https://www.youtube.com/watch?v=BaW_jenozKc',"https://www.youtube.com/watch?v=3m7ZUL8zJSc"]
    #URLS = ['https://www.youtube.com/PointCrow','https://www.youtube.com/watch?v=BaW_jenozKc',"https://www.youtube.com/watch?v=3m7ZUL8zJSc"]
    ydl = YoutubeDL()
    #with YoutubeDL() as ydl:
    os.chdir("C://Users//amaha//VS_Python_Projects//discord_image_bot//videos")
    for url in URLS:
        #print("entering try except")
        try:
            #print(type(url))
            #print(type(URLS))          
            #print("downloading this", url)
            # Get the duration of the video in seconds
            new_url = url.replace("'",'')
            yt = YouTube(new_url)
            video_length = yt.length
            print("length of video", video_length)
            # Check if the duration is longer than 10 minutes
            if video_length < 600:
                ydl.download(new_url)
        except Exception as e:
            print(f"Could not download {new_url}")
            #print(Exception)


#read_txt_file()
f = open('Filtered_DMs.txt','r', encoding='utf8')
    #download(f)
#print(f.readlines())

data = f.read()
print(type(data))
data_split = data.split(',')
#print(data_split)
print(type(data_split))
download(data_split)
#print(data_split[456])
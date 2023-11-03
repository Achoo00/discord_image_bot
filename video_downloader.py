from yt_dlp import YoutubeDL
import re
#Stuff to do
#1. Still need to remove text before https
#2. UnicodeDecodeError txt file has weird characters in it,find some way of deleting it or change encoding - done
#3. Get rid of channel link


#Types of urls
#https://www.youtube.com/watch?v=Vr54kmrnCFU
#https://youtu.be/Ks2UnT4Nzcs
#https://youtube.com/playlist?list=PLZ34fLWik_iASrR26p_41rirqp8GkPAr_

#Youtube urls will always have 11 characters after "watch?v=" or after "be/" or after "shorts/"

# Stuff to read on
#https://www.w3schools.com/python/ref_string_rsplit.asp
#https://codefather.tech/blog/python-check-for-duplicates-in-list/?expand_article=1

urls=[]
clean_list = []

def download():
    URLS = ['https://www.youtube.com/watch?v=Hko7bqYiJow (private)','https://www.youtube.com/@MizkifYT','https://www.youtube.com/watch?v=BaW_jenozKc',"https://www.youtube.com/watch?v=3m7ZUL8zJSc"]
    #URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc',"https://www.youtube.com/watch?v=3m7ZUL8zJSc"]
    with YoutubeDL() as ydl:
        ydl.download(URLS)

def check_youtube_vid(f):
    i=0
    for line in f:
        if 'youtu' in line:
            i=i+1
            if 'share' not in line:
                pass
                if 'playlist' not in line:
                    org_line = line.strip()
                    new_line = org_line

                    urls.append(line.strip())
                    print(line.strip())
    print(type(urls))
    print("the urls:",urls)
        #    if 'share' in line:

def remove_unrelated_links(f):
    # Use a list comprehension to filter out the urls that contain 'https' and 'youtu' but not 'channel', '@', '/c/' or 'playlist'
    #used re.sub to get rid of all characters before https
    list_without_playlist = [re.sub(r'^.*?https', 'https', line.strip()) for line in f if 'https' in line and 'youtu' in line and not any(x in line for x in ['channel', '@', '/c/', 'playlist'])]
    print("the urls", list_without_playlist)

def read_txt_file():
    with open('DMs.txt',encoding='utf8') as f: #Change encoding to utf8 because there are some weird characters to read
        try:
            remove_unrelated_links(f)
        except UnicodeDecodeError:
            print("could not read character")

read_txt_file()
#download()

#Tests for duplicates
#print(len(urls))
#print(len(set(urls)))

from yt_dlp import YoutubeDL
import re
#Stuff to do
#1. UnicodeDecodeError txt file has weird characters in it,find some way of deleting it or change encoding - done
#2. Anything longer than 10 minutes is skipped ex: 7h livestream 'https://www.youtube.com/watch?v=Hko7bqYiJow (private)'


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

def remove_unrelated_links(f):
    # Use a list comprehension to filter out the urls that contain 'https' and 'youtu' but not 'channel', '@', '/c/' or 'playlist'
    #used re.sub to get rid of all characters before https
    list_without_playlist = [re.sub(r'^.*?https', 'https', line.strip()) for line in f if 'https' in line and 'youtu' in line and not any(x in line for x in ['channel', '@', '/c/', 'playlist'])]
    print("the urls", list_without_playlist)
    with open('Filtered_DMs.txt', 'w', encoding='utf8') as f:
        f.write(str(list_without_playlist))

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

import re
import requests

urls=["asdasdsad https://www.youtube.com/channel/UC9ruVYPv7yJmV0Rh0NKA-Lw",
"wejhiwuehbrf https://www.youtube.com/channel/UCJd7dGbOFMI3tnr5KL4zEEQ",
"0123947012 nj https://www.youtube.com/channel/UCz4jhqrCfthF8NnldZeK_rw",
"98y 9sahf 98ah f9uh2 https://www.youtube.com/watch?v=D6DVTLvOupE",
"#!$DSF # 2 rfsd https://youtube.com/shorts/ksKayAeQ6LQ?feature=share",
"https://www.youtube.com/shorts/ksKayAeQ6LQ",
"https://www.youtube.com/playlist?list=PLz23nO6Hjlf84amtkQA79Dlx-jjTk17ws",
"https://youtu.be/fyrK7CCF5yU"]

#urls.remove("https://www.youtube.com/channel/UCJd7dGbOFMI3tnr5KL4zEEQ")
#print(urls)

list_without_channel = []
list_without_playlist = []
clean_list = []
#Without list comprehension

def no_list_comprehension():
    for url in urls:
        if 'channel' not in url:
            list_without_channel.append(url)

    for url in list_without_channel:
        if 'playlist' not in url:
            list_without_playlist.append(url)

#With list comprehension, cuts down on lines

def list_comprehension():
    newlist = [x for x in urls if 'channel' not in x]
    newerlist = [x for x in newlist if 'playlist' not in x]
    print(newerlist)
    for url in newerlist:
        clean = re.sub(r'^.*?https', 'https', url) #something to do with regex and removing every character before "https"
        clean_list.append(clean)
    print(clean_list)

#list_comprehension()
#url = "https://youtube.com/shorts/pZFoVjZZ9qc?feature=share"
url = "https://www.youtube.com/w"
#url = "https://www.youtube.com/watch?v=MTCC2S5onHc&t=2794s"
#url = "https://youtube.com/pointcrowvods"
#url = "https://www.youtube.com/watch?v=BPvD-dfIiEs"

r = requests.get(url) # random video id
print("Video unavailable" in r.text)

#stri = "asiuhaishdI'm"
#new_stri = re.sub(r'^.*?I', 'I', stri) #something to do with regex and removing every character before "I"
#print(new_stri)
#lsdhaosdo ash
from pytube import YouTube
from sys import argv

link = argv[1]

yt = YouTube(link)

print("Title: ", yt.title)
print("Author: ", yt.author)

yd = yt.streams.get_highest_resolution()

yd.download("/Users/tngo/Desktop")

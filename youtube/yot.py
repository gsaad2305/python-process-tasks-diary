from pytubefix import YouTube
from pytubefix .cli import on_progress

url = input("Cole a url do video: ")
yt = YouTube(url, on_progress_callback=on_progress)
ys = yt.streams.get_audio_only()

print(yt.title)
ys.download("/home/saadlinux/")
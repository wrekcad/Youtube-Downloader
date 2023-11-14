from pytube import YouTube
from sys import argv

link = argv[1]
method = argv[2]

yt = YouTube(link)

print("Title: ", yt.title)

print('Views: ', yt.views)

if method == 'mp3':
    print('Downloading audio from user: ', yt.author, '...')
    yd = yt.streams.get_audio_only()
    yd.download('download')
    print('video: ', yt.title, 'done downloading!')
elif method == 'mp4':
    print('Downloading video from user: ', yt.author, '...')
    yd = yt.streams.get_highest_resolution()
    yd.download('download')
    print('video: ', yt.title, 'done downloading!')



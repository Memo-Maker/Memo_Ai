from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=rd0I-sFlclw')

yt.streams.filter(only_audio=True).first().download(
    output_path='.', filename='input.mp3')
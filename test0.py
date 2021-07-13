from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=34Ey4i3wp-8')
print(yt.streams)

from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=34Ey4i3wp-8')
# ~ lst = []

# ~ for i in range(len(yt.streams)):
	# ~ lst.append(str(yt.streams[i]).split())
# ~ print(lst)
yt.streams.get_by_itag(140).download()



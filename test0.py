from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=34Ey4i3wp-8')
# ~ x = str(yt.streams[0]).split()
lst = []

for i in range(len(yt.streams)):
	lst.append(str(yt.streams[i]).split())
print(lst)



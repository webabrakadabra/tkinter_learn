#!/usr/bin/env python3

import pytube


url = input('ВВедіть адресу кліпу: \n')

try:
	youtube = pytube.YouTube(url)
	video = youtube.streams.first()
	print('Кліп:', youtube.title, 'розміром', youtube.length, 'буде завантажено в /home/grey/Відео/clips')
	video.download('E:/')
	print('Кліп завантажено')
except Exception:
	print('Щось пішло не так......')
	



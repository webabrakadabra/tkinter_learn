#!/usr/bin/env python3

from tkinter import filedialog
from tkinter import *
import pyautogui
import pytube
import time
from threading import Thread

global x
global x2

def insert():
    pyautogui.hotkey('ctrl', 'v')
    txt1.delete(0, 'end')

def browse_button():
    filename = filedialog.askdirectory()
    txt2.delete(0, 'end')
    txt2.insert(0, filename)
    
def download():
    x = txt1.get()
    x2 = txt2.get()
    try:
        youtube = pytube.YouTube(x)
        video = youtube.streams.filter(res="720p").first()
        print('Кліп:', youtube.title, 'розміром', youtube.length, 'буде завантажено в /home/grey/Відео/clips')
        lb3.config(text = "Завантаження:" + youtube.title)
        # ~ window.update()
        video.download(x2)
        #window.update()
        lb3.config(text = "Відео: " + youtube.title + " завантажено")
        print('Кліп завантажено')
        
    except Exception:
        print('Щось пішло не так......')
        
def starter():
	Thread(target=download,args=()).start()

    


window = Tk()
window.title("Програма загрузки роликів з YouTube")
window.configure(background='bisque')
# ~ window.geometry("700x200")
window.resizable(False, False)
lb1 = Label(window, text="Вставте скопійоване посилання на відео з Youtube:", font=("Times New Roman", 14))
lb2 = Label(window, text="Виберіть директорію для збереження відео:", font=("Times New Roman", 14))
lb3 = Label(window, font=("Times New Roman", 14))
lb1.configure(background='bisque')
lb2.configure(background='bisque')
lb1.grid(column=0, row=0, padx=(10, 0))
lb2.grid(column=0, row=2, padx=(10, 0))
lb3.grid(column=0, row=5, padx=(10, 0), pady=(10, 10))

btn1 = Button(window, text="Завантажити", width=40, command=starter)
btn2 = Button(window, text="Вставити", command=insert)
btn3 = Button(window, text="Вибрати", command=browse_button)
btn1.grid(column=0, row=4, padx=(10, 10))
btn2.grid(column=2, row=1, padx=(10, 10))
btn3.grid(column=2, row=3, padx=(10, 10))

txt1 = Entry(window, width=70, bd=2)
txt2 = Entry(window, width=70, bd=2)
txt1.grid(column=0, row=1, padx=(10, 10))
txt2.grid(column=0, row=3, padx=(10, 10), pady=(0, 10))



window.mainloop()

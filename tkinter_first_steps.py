#!/usr/bin/env python3

from tkinter import filedialog
from tkinter import *
import pyautogui
import pytube
import time

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
        video = youtube.streams.first()
        print('Кліп:', youtube.title, 'розміром', youtube.length, 'буде завантажено в /home/grey/Відео/clips')
        video.download(x2)
        print('Кліп завантажено')
    except Exception:
        print('Щось пішло не так......')

window = Tk()
window.title("Програма загрузки роликів з YouTube")
window.configure(background='bisque')
window.geometry("540x200")
lb1 = Label(window, text="Вставте скопійоване посилання на відео з Youtube:", font=("Times New Roman", 14))
lb2 = Label(window, text="Виберіть директорію для збереження відео:", font=("Times New Roman", 14))
lb1.configure(background='bisque')
lb2.configure(background='bisque')
lb1.grid(column=0, row=0, padx=(10, 0))
lb2.grid(column=0, row=2, padx=(10, 0))

btn1 = Button(window, text="Завантажити", width=40, command=download)
btn2 = Button(window, text="Вставити", command=insert)
btn3 = Button(window, text="Вибрати", command=browse_button)
btn1.grid(column=0, row=4)
btn2.grid(column=2, row=1)
btn3.grid(column=2, row=3)

txt1 = Entry(window, width=70, bd=2)
txt2 = Entry(window, width=70, bd=2)
txt1.grid(column=0, row=1, padx=(10, 10))
txt2.grid(column=0, row=3, padx=(10, 10), pady=(0, 10))

window.mainloop()


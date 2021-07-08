#!/usr/bin/env python3

from tkinter import *
import pyautogui

def insert():
	pyautogui.hotkey('ctrl', 'v')
	
window = Tk()
window.title("Текст0")
window.geometry("540x200")
lb1 = Label(window, text="Вставте скопійоване посилання на відео з Youtube:", font=("Times New Roman", 14))
lb2 = Label(window, text="Виберіть директорію для збереження відео:", font=("Times New Roman", 14))
lb1.grid(column=0, row=0, padx=(10, 0))
lb2.grid(column=0, row=2, padx=(10, 0))

btn1 = Button(window, text="Завантажити", width=40)
btn2 = Button(window, text="Вставити", command=insert)
btn3 = Button(window, text="Вибрати")
btn1.grid(column=0, row=4)
btn2.grid(column=2, row=1)
btn3.grid(column=2, row=3)

txt1 = Entry(window, width=51)
txt2 = Entry(window, width=51)
txt1.grid(column=0, row=1, padx=(10, 10))
txt2.grid(column=0, row=3, padx=(10, 10), pady=(0, 10))



window.mainloop()


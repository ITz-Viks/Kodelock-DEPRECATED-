#!/bin/python3

from pathlib import Path

from tkinter import *
from PIL import ImageTk, Image
from pynput import keyboard


# Placeholder & Files
codes = "codes.txt"
code_list = Path(codes).read_text().splitlines()

CodeFace  = Image.open("./imgs/Face.jpg")
LeftArrow  = Image.open("./imgs/LeftArr.png")
RightArrow = Image.open("./imgs//RightArr.png")

# Settings
app = Tk()
app.geometry("400x580")
app.title("Kodelock")


# Commands
def next():
    SF = int(Start_from.get())
    SF = SF+1
    current_code['text'] = code_list[SF]
    Start_from.delete(0, "end")
    Start_from.insert(0, SF)

def pre():
    SF = int(Start_from.get())
    SF = SF-1
    current_code['text'] = code_list[SF]
    Start_from.delete(0, "end")
    Start_from.insert(0, SF)

def SET():
    SF = int(Start_from.get())
    current_code['text'] = code_list[SF]
    Start_from.delete(0, "end")
    Start_from.insert(0, SF)


# Essential
Face = ImageTk.PhotoImage(CodeFace)
CodeFace = Label(image=Face)
rightkey = Label(app, text="Bind:\n RKey", font=("Ariel",10))
leftkey = Label(app, text="Bind:\n LKey", font=("Ariel",10))
Start_fromL = Label(app,text="Start From:", font=("Ariel",13),bg="#f55919")
Set = Button(app,text="Set", command=SET)

# Start From: , Current: , and Code display
current_code = Label(app, text="", font=("Ariel",30), bg="black", fg="white")
Start_from = Entry(app, bg="red", font=("Ariel",18))

# Arrow buttons
resized_left = LeftArrow.resize((55, 42))
Left = ImageTk.PhotoImage(resized_left)
leftbutton = Button(app, image=Left,bg="#f55919", command=pre)

resized_right = RightArrow.resize((55, 42))
Right = ImageTk.PhotoImage(resized_right)
rightbutton = Button(app, image=Right,bg="#f55919", command=next)

# Body
CodeFace.place(x=-63, y=-65)
leftbutton.place(x=1,y=534, width=60, height=45)
rightbutton.place(x=340,y=534, width=60, height=45)
current_code.place(x=114,y=76,width=176,height=30)
Start_from.place(x=200,y=534, width=70, height=45)
rightkey.place(x=302,y=534,width=38, height=45)
leftkey.place(x=59,y=534,width=38, height=45)
Start_fromL.place(x=115,y=534,width=85,height=45)
Set.place(x=268,y=534,width=25,height=45)

# Launcher and keybinds
COMBINATIONS = [
    {keyboard.Key.right}
]
COMBINATIONS2 = [
    {keyboard.Key.left}
]
current = set()
current2 = set()

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            next()
    elif any([key in COMBO1 for COMBO1 in COMBINATIONS2]):
        current2.add(key)
        if any(all(k1 in current2 for k1 in COMBO1) for COMBO1 in COMBINATIONS2):
            pre()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    Start_from.insert(0, 0)
    app.mainloop()
    listener.join()

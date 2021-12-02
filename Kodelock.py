"""

CHANGELOG:  v2
( Linux support is here because my school issued laptop is linux, not because it may be relevant to rust in some way )

1. When exiting, the code you were at gets saved and will show when re-opened
    1.1 Changed some variables and operators for optimizations
    1.2 Added functions count, write in order to keep the line number for codes.txt after exiting
2. Added config folder for further usage and organisement
3. Fixed a missing if statement for on_release()
4. Directories are now managed by pathlib 
    4.1 List is now managed by path as suggested by @christopherwoodall
5. Added icon
6. Upgraded overall looks.
    6.1 Arrows changed from black to red
    6.2 Main background and arrow button background changed to white
    6.3 Minor placement changes
    6.4 Adjusted border width on buttons
    6.5 Color adjustments around "Start From" feature
7. Added a keybind to allow -Start From to be set with Enter instead of only the set button
8. Added multiple Tabs
    8.1 Main part was added to a frame and that frame to a notebook 
    8.2 Added Usage and Info Tabs
9. Changed keybinds from pynput to the tkinter .bind that I missed in the documentation, before.

"""

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image 
from pathlib import Path

# Placeholders
root = Tk()
cwd = Path.cwd()

# Notebook 
Notebook = ttk.Notebook(root)

Main = Frame(Notebook)
Usage = Frame(Notebook)

Notebook.add(Main,text="Main")
Notebook.add(Usage,text="Usage & Info")
Notebook.pack(side=TOP, anchor=NW,expand=True,fill="both")



# Files
codes = (cwd / "config/codes.txt")
CodeFace = Image.open(cwd / "imgs/Face.jpg")
LeftArrow = Image.open(cwd / "imgs/new_left.png")
RightArrow = Image.open(cwd / "imgs/new_right.png")
counter = open(cwd / "config/counter.txt", "r")
icon = Image.open(cwd / "imgs/icon.png")
sfc = Image.open(cwd / "imgs/sc.png")

# Settings
root.geometry("400x600")
root.title("Kodelock")
root.iconphoto(False, PhotoImage(file=cwd / 'imgs/icon.png'))
root["bg"] = "white"

# Commands
def count():
    c = int(counter.read())
    current_code['text']= code_list[c]
    Start_from.delete(0, "end")
    Start_from.insert(0, c)
    counter.close

def write():
    countr = int(Start_from.get())
    counter_file = open(cwd / "config/counter.txt", "w")   
    counter_file.write(str(countr))
    
def next(root):
    SF = int(Start_from.get())
    SF += 1
    current_code['text']= code_list[SF]
    Start_from.delete(0, "end")
    Start_from.insert(0, SF)
    write()
    
def pre(root):
    SF = int(Start_from.get())
    SF -= 1
    current_code['text']= code_list[SF]
    Start_from.delete(0, "end")
    Start_from.insert(0, SF)
    write()

def SET(root):
    SF = int(Start_from.get())
    current_code['text']= code_list[SF]
    Start_from.delete(0, "end")
    Start_from.insert(0, SF)
    write()

# List Handler
code_list = Path(codes).read_text().splitlines()

# Essential
Face = ImageTk.PhotoImage(CodeFace) 
CodeFace = Label(Main,image=Face)
rightkey = Label(Main, text="Bind:\n RKey",bg="white", font=("Ariel",10))

leftkey = Label(Main, text="Bind:\n LKey", bg="white", font=("Ariel",10))
Start_fromL = Label(Main,text="Start\n From:", font=("Ariel",12),bg="white")   ##f55919
Set = Button(Main,text="Set", command=SET, bd=0.5, activebackground='#345',activeforeground='white')

# Start From: , Current: , and Code display
current_code = Label(Main, text="", font=("Ariel",30), bg="black", fg="white")
Start_from = Entry(Main, bg="#EBF4F4", font=("Ariel",18), bd=0.5)

# Arrow buttons 
resized_left = LeftArrow.resize((55, 42))
Left = ImageTk.PhotoImage(resized_left)
leftbutton = Button(Main, image=Left,bg="white",bd=0,highlightthickness=0, command=lambda: pre(root)) 

resized_right = RightArrow.resize((55, 42))
Right = ImageTk.PhotoImage(resized_right)
rightbutton = Button(Main, image=Right,bg="white", bd=0,highlightthickness=0, command=lambda: next(root))

# Usage TAB
SCF = ImageTk.PhotoImage(sfc)

canvas = Canvas(Usage, bg="white", height=600,width=400)

canvas.create_text(60, 20, text="Keybinds:", fill="black", font=("Ariel", 19))
canvas.create_image(30, 70, image=Left)
canvas.create_text(70, 100, text="Moves backwards", fill="black", font=("Ariel", 13))

canvas.create_image(320, 70, image=Right)
canvas.create_text(320, 100, text="Moves Forwards", fill="black", font=("Ariel", 13))

canvas.create_image(200, 220, image=SCF)
canvas.create_text(1, 270, anchor=NW, text="This part is used if you wish to use this tool with multiple people.\n You put in the number of a code you want to start from. \n For Example\n Person 1 starts from 0 and punches the codes from 0-500 in\n Person 2 punches the codes from 500-100 in, and so on...", fill="black", font=("Ariel", 9))

canvas.create_text(1, 370, anchor=NW, text="Script made by ITzViks \nGithub: https://github.com/ITz-Viks/Kodelock", font=("Ariel", 12))


canvas.pack()

# Body
CodeFace.place(x=-63, y=-65)
leftbutton.place(x=1,y=534, width=60, height=45)
rightbutton.place(x=340,y=534, width=60, height=45)
current_code.place(x=114,y=71,width=176,height=40)
rightkey.place(x=302,y=534,width=38, height=45)
leftkey.place(x=59,y=534,width=38, height=45)
Start_from.place(x=180,y=534, width=70, height=45)
Start_fromL.place(x=102,y=534,width=90,height=45)
Set.place(x=248,y=534,width=25,height=45)

# Binds
root.bind("<Left>", pre)
root.bind("<Right>", next)
root.bind("<Return>", SET)

    # Disables traversal between tabs with Left and Right arrows as they're already being used.
Notebook.bind("<Left>", lambda e: "break")
Notebook.bind("<Right>", lambda e: "break")

# Launcher
    # Sets the code to the one before exiting
count()
    # Starts everything
root.mainloop()


import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3
root=Tk()
root.minsize(300,300)

listofsongs= []
realnames= []
v=StringVar()
songlabel=Label(root,textvariable=v,width=50)
index=0

def nextsong(event):
    global index
    index +=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")



def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    return songname

def directorychooser():
    directory  = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir=os.path.realpath(files)
            audio=ID3(realdir)
            realnames.append(audio["TIT2"].text[0])

            listofsongs.append(files)
            print (files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()
directorychooser()


label =Label(root, text="Music Player",fg="red",bg="sky blue")
label.config(font=("Comic Sans MS", 20), height=1, width=80)
label.pack(pady=10, padx=10)

listbox=Listbox(root)
listbox.pack()

realnames.reverse()
for items in realnames:
    listbox.insert(0,items)
realnames.reverse()
directorychooser()


nextbutton=Button(root,text="Next Song")
nextbutton.pack()

previousbutton = Button(root, text="Previous Song")
previousbutton.pack()

stopbutton = Button(root, text="Stop Music")
stopbutton.pack()

nextbutton.bind("<Button-1>", nextsong)
previousbutton.bind("<Button-1>", prevsong)
stopbutton.bind('<Button-1>', stopsong)

songlabel.pack()
root.mainloop()
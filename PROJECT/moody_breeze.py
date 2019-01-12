from tkinter import *
import tkinter
import  tkinter as Tk
import tkinter.messagebox as mb
import os
import pygame
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3
import sqlite3
index=0
listofsongs=[]
realnames=[]

db = sqlite3.connect('Profiles')
cursor1 = db.cursor()
cursor2 = db.cursor()

#cursor1.execute('''CREATE TABLE customers(name TEXT,email TEXT, phone_no TEXT, password TEXT)''')
class SeaofBTCapp(Tk.Tk):

    def __init__(self, *args, **kwargs):

        Tk.Tk.__init__(self, *args, **kwargs)

        container = Tk.Frame(self,bg = 'white')

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree ):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(Tk.Frame):

    def __init__(self, parent, controller):
        Tk.Frame.__init__(self,parent)

        l=Label(self,text="MOODY BREEZE",fg="white",bg="black")
        l.config(font=("Snap ITC",30),height=5,width=200)
        l.pack(pady=10,padx=10)
        lab=Label(self,text="MUSIC FOR EVERYONE",fg="black",bg="red")
        lab.config(font=("Rockwell Extra Bold",20),height=1,width=80)
        lab.pack(pady=5,padx=5)
        l1=Label(self,text="USERNAME",fg="black",anchor="center",bg="sky blue")
        l1.config(font=("AR CENA",15),height=1,width=50)
        l1.pack(pady=5,padx=5)
        E1=Entry(self,bd=5)
        E1.config(font=("Courier",10),width=50)
        E1.pack(pady=5,padx=5)

        l2=Label(self,text="PASSWORD",fg="black",anchor="center",bg="sky blue")
        l2.config(font=("AR CENA",15),height=1,width=50)
        l2.pack(pady=10,padx=10)
        E2=Entry(self,bd=5,show="*")
        E2.config(font=("Courier",10),width=50)
        E2.pack(pady=10,padx=10)
        def ok3():
            if cursor1.execute('''SELECT password FROM customers WHERE name=?''', (E1.get(),)):
                print ("Record fetched successfully")

            pwd = str(cursor1.fetchone())
            #print (pwd)
            pwd1 = str(E2.get())
            #print (pwd1)
            pwd2 = "('" + pwd1 + "',)"

            if (pwd2 == pwd):
                mb.showwarning("Correct", "You have successfully logged in")
                controller.show_frame(PageTwo)
            else:
                mb.showwarning("Incorrect", "Incorrect username or password")

        button1=Button(self,text="SIGN IN",bg="black",fg="white",command=ok3)
        button1.config(font=("Courier",10),width=50)
        button1.pack(pady=10,padx=10)


        button2=Button(self,text="SIGN UP",bg="black",fg="white",command=lambda:controller.show_frame(PageOne))
        button2.config(font=("Courier",10),width=50)
        button2.pack(pady=10,padx=10)
        l3=Label(self,text="MUSIC,at its essence,is what gives us memories.",fg='red',bg="white")
        l3.config(font=("Courier",20),height=1,width=100)
        l3.pack(pady=10,padx=10)

class PageOne(Tk.Frame):

    def __init__(self, parent, controller):
        Tk.Frame.__init__(self, parent)
        l4 = Label(self, text="MOODY BREEZE", fg="white", bg="black")
        l4.config(font=("Snap ITC", 30), height=2, width=200)
        l4.pack(pady=5, padx=5)
        l5 = Label(self, text="INDIA'S NO. 1 MUSIC STORE!!", fg="red", bg="sky blue")
        l5.config(font=("Rockwell Extra Bold", 15), height=2, width=80)
        l5.pack(pady=5, padx=5)
        l6 = Label(self, text="Songs to suit every moods and occasions", fg="red", bg="sky blue")
        l6.config(font=("Georgia", 13), height=1, width=80)
        l6.pack(pady=5, padx=5)
        l7 = Label(self, text="JOIN US", fg="sky blue", bg="black")
        l7.config(font=("Rockwell Extra Bold", 15), height=1, width=40)
        l7.pack(pady=5, padx=5)
        l8 = Label(self, text="USERNAME", fg="red", bg="light green")
        l8.config(font=("AR CENA", 15), height=1, width=50)
        l8.pack(padx=5, pady=5)
        E3 = Entry(self, bd=5, fg="black")
        E3.config(font=("Courier", 10), width=50)
        E3.pack(pady=5, padx=5)
        l9 = Label(self, text="EMAIL ID", fg="red", bg="light green")
        l9.config(font=("AR CENA", 15), height=1, width=50)
        l9.pack(padx=5, pady=5)
        E4 = Entry(self, bd=5, fg="black")
        E4.config(font=("Courier", 10), width=50)
        E4.pack(pady=5, padx=5)
        l10 = Label(self, text="MOBILE NUMBER", fg="red", bg="light green")
        l10.config(font=("AR CENA", 15), height=1, width=50)
        l10.pack(padx=5, pady=5)
        E5 = Entry(self, bd=5, fg="black")
        E5.config(font=("Courier", 10), width=50)
        E5.pack(pady=5, padx=5)
        l11 = Label(self, text="PASSWORD", fg="red", bg="light green")
        l11.config(font=("AR CENA", 15), height=1, width=50)
        l11.pack(padx=5, pady=5)
        E6 = Entry(self, bd=5, fg="black", show="*")
        E6.config(font=("Courier", 10), width=50)
        E6.pack(pady=5, padx=5)

        def register():
            mb.showinfo("CONGRATULATIONS", "Successfully Registered")
            if cursor1.execute('''INSERT INTO customers(name,email,phone_no,password)VALUES(?,?,?,?)''',(E3.get(),E4.get(),
            E5.get(),E6.get())):
                print ("Values inserted successfully")
            db.commit()

        button3 = Button(self, text="REGISTER", bg="black", fg="white", command=register)
        button3.config(font=("Courier", 10), width=50)
        button3.pack(pady=5, padx=5)
        button4 = Button(self, text="BACK TO HOME PAGE", bg="black", fg="white",command=lambda:controller.show_frame(StartPage) )
        button4.config(font=("Courier", 10), width=50)
        button4.pack(pady=5, padx=5)

class PageTwo(Tk.Frame):
    global v
    def __init__(self, parent, controller):
        Tk.Frame.__init__(self, parent, bg="white")
        l12 = Label(self, text="MOODY BREEZE", fg="white", bg="black")
        l12.config(font=("Snap ITC", 30), height=3, width=200)
        l12.pack(pady=5, padx=5)

        l13 = Label(self, text="PLAYLISTS", fg="red", bg="sky blue")
        l13.config(font=("Rockwell Extra Bold", 30), height=2, width=200)
        l13.pack(pady=5, padx=5)

        def directorychooser():
            global directory

            directory = askdirectory()
            os.chdir(directory)

            for files in os.listdir(directory):
                if files.endswith(".mp3"):
                    realdir = os.path.realpath(files)
                    audio = ID3(realdir)
                    realnames.append(audio["TIT2"].text[0])

                    listofsongs.append(files)
                    # print(files)

            pygame.mixer.init()
            pygame.mixer.music.load(listofsongs[0])
            pygame.mixer.music.play()


            controller.show_frame(PageThree)



        button5 = Button(self, text="LATEST SONGS", fg="blue", bg="pink",command=directorychooser)
        button5.config(font=("Showcard Gothic", 15), width=50)
        button5.pack(pady=5, padx=5)

        button6 = Button(self, text="ROCK!!", fg="blue", bg="pink",command=directorychooser)
        button6.config(font=("Showcard Gothic", 15), width=50)
        button6.pack(pady=5, padx=5)

        button7 = Button(self, text="ROMANTIC", fg="blue", bg="pink",command=directorychooser)
        button7.config(font=("Showcard Gothic", 15), width=50)
        button7.pack(pady=5, padx=5)

        button8 = Button(self, text="DEVOTIONAL", fg="blue", bg="pink",command=directorychooser)
        button8.config(font=("Showcard Gothic", 15), width=50)
        button8.pack(pady=5, padx=5)

        l14 = Label(self, text="Music is the divine way to tell beautiful, poetic things to the heart.", fg='red',
                    bg="white")
        l14.config(font=("Comic Sans MS", 20), height=1, width=80)
        l14.pack(pady=10, padx=10)

    def nextsong(event):
        global index
        index += 1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()


    def prevsong(event):
        global index
        index -= 1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()


    def stopsong(event):
        pygame.mixer.music.stop()




class PageThree(Tk.Frame):


    def __init__(self, parent, controller):
        Tk.Frame.__init__(self,parent)
        v=StringVar()
        songlabel = Label(self, textvariable=v, width=50)


        '''

        def nextsong(event):
            global index
            index += 1
            pygame.mixer.music.load(listofsongs[index])
            pygame.mixer.music.play()
            updatelabel()

        def prevsong(event):
            global index
            index -= 1
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


'''

        labelm=Label(self,text="MOODY BREEZE",fg="white",bg="black")
        labelm.config(font=("Snap ITC",30),height=4,width=200)
        labelm.pack(pady=5,padx=5)



        label = Label(self, text="MUSIC PLAYER", fg="red", bg="sky blue")
        label.config(font=("AR CENA", 25), height=2, width=80)
        label.pack(pady=10, padx=10)






        nextbutton = Button(self, text="Next Song",fg="black",bg="red")
        nextbutton.config(font=("Comic Sans MS", 20), height=1, width=50)
        nextbutton.pack(padx=10,pady=10)

        previousbutton = Button(self, text="Previous Song",fg="black",bg="red")
        previousbutton.config(font=("Comic Sans MS", 20), height=1, width=50)
        previousbutton.pack(padx=10,pady=10)

        stopbutton = Button(self, text="Stop Music",fg="black",bg="red")
        stopbutton.config(font=("Comic Sans MS", 20), height=1, width=50)
        stopbutton.pack(padx=10,pady=10)

        nextbutton.bind("<Button-1>", PageTwo.nextsong)
        previousbutton.bind("<Button-1>", PageTwo.prevsong)
        stopbutton.bind('<Button-1>', PageTwo.stopsong)


        songlabel.pack()
app=SeaofBTCapp()
app.mainloop()
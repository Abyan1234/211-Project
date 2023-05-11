#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from playsound import playsound
import ftplib
from ftplib import FTP
import pygame
from pygame import mixer
import ntpath
from pathlib import Path
import os
import time




PORT  = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load(('shared_file/'+song_selected))
    mixer.music.pause()
    infoLabel.configure(text="")

def play():
    global song_selected
    song_selected=listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load(('shared_file/'+song_selected))
    mixer.music.play()
    if(song_selected != ""):
        infoLabel.configure(text="Now Playing: "+song_selected)
    else:
        infoLabel.configure(text="")

def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()



def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()


def browseFiles():
    global textarea
    global filePathLabel

    try:
        filename=filedialog.askopenfilename()
        filePathLabel.configure(text=filename)

        hostname="127.0.0.1"
        userid="lftpd"
        userpassword="lftpd"
        ftpserver=FTP(hostname,userid,userpassword)
        ftpserver.encoding="utf-8"
        ftpserver.cwd('shared_files')
        fname=ntpath.basename(filename)
        with open(filename,'rb') as f:
            ftpserver.storbinary(fname,f)
        ftpserver.dir()
        ftpserver.quit()

    except FileNotFoundError:
        print("Cancel button pressed") 

def musicWindow():

   
    print("\n\t\t\t\tIP MESSENGER")

    #Client GUI starts here
    window=Tk()

    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg='LightSkyBlue')

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel
    global infoLabel

    selectlabel = Label(window, text= "Select Song",bg='LightSkyBlue', font = ("Calibri",8))
    selectlabel.place(x=2, y=1)

    listbox = Listbox(window,height = 9,width = 39,activestyle = 'dotbox',bg='LightSkyBlue',borderwidth=2, font = ("Calibri",10))
    listbox.place(x=10, y=20)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    playButton=Button(window,text="Play",width=10,bd=1,bg='SkyBlue', font = ("Calibri",10),command=play)
    playButton.place(x=30,y=200)

    
    ResumeButton=Button(window,text="Resume",width=10,bd=1,bg='SkyBlue', font = ("Calibri",10),command=resume)
    ResumeButton.place(x=30,y=250)

    PauseButton=Button(window,text="Resume",width=10,bd=1,bg='SkyBlue', font = ("Calibri",10),command=pause)
    PauseButton.place(x=200,y=250)

    Stop=Button(window,text="Stop",width=10,bd=1,bg='SkyBlue', font = ("Calibri",10),command=stop)
    Stop.place(x=200,y=200)

    Upload=Button(window,text="Upload",width=10,bd=1,bg='SkyBlue', font = ("Calibri",10))
    Upload.place(x=30,y=250)

    Download=Button(window,text="Download",width=10,bd=1,bg='SkyBlue', font = ("Calibri",10))
    Download.place(x=200,y=250)

    selectlabel = Label(window, text= "",fg='blue', font = ("Calibri",8))
    selectlabel.place(x=4, y=200)

    infoLabel= Label(window, text="",fg="blue",font=("Calibri",0))
    infoLabel.place(x=100,y=200)

  
    window.mainloop()


musicWindow()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    musicWindow()

setup()

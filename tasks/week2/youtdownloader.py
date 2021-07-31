from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
from tkinter import ttk
import youtube_dl
from pytube import YouTube

#pip install pytube3

Folder=""

#File Location
def openLocation():
    global Folder
    Folder=filedialog.askdirectory()
    if(len(Folder)>1):
        locationError.config(text=Folder,fg="green")
    else:
        locationError.config(text="Please select a folder",fg="red")

#Video Download
def downloadVideo():
    quality =ytdQuality.get()
    url=ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="",fg="green")
        yt=YouTube(url)

        if(quality==quality[0]):
            select=yt.streams.filter(progressive=True).first()
        elif(quality==quality[1]):
            select=yt.streams.filter(progressive=True,file_extension="mp4").last()
        elif(quality==quality[2]):
            select=yt.streams.filter(only_audio=True).first()
        else:
            ytdError.config(text="Please paste link again",fg="red")

#Downloading function
    select.download(Folder)
    ytdError.config(text="Download completed",fg="green")


root=Tk()
root.title("Morris' Youtube Downloader")
root.geometry("500x300")
root.resizable(True, True)
root.configure(background = "black")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


ytdLabel=Label(root, text="Enter URL", bg="black", fg="white", font="none 18 bold")
ytdLabel.grid()

ytdYourUrl=StringVar()
ytdEntry=Entry(root, textvariable=ytdYourUrl, width=50)
ytdEntry.grid()

ytdError=Label(root, text="Error!", bg="red", fg="white", font="none 14 bold")
ytdError.grid()


saveLabel=Label(root, text="Save", bg="black", fg="white", font="none 18 bold")
saveLabel.grid()

saveButton=Button(root, text="Select Path",width=10, background="black", fg="white", font="none 14 bold",command=openLocation)
saveButton.grid()

locationError=Label(root, text="Location path error",bg="red", fg="white", font="none 14 bold")
locationError.grid()

ytdQuality=Label(root, text="Quality", bg="black", fg="white", font="none 18 bold")
ytdQuality.grid()

quality=["720p","144p","Only Audio"]
ytdQuality=ttk.Combobox(root,values=quality, width=10)
ytdQuality.grid()

downloadButton=Button(root, text="Download",width=10, background="black", fg="white", font="none 14 bold",command=downloadVideo)
downloadButton.grid()

MorrisLabel=Label(root, text="Created by Morris-Lux Academy", bg="black", fg="white", font="none 10 bold")
MorrisLabel.grid()

root.mainloop()
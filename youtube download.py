from cProfile import label
from cgitb import text
from tkinter import*
from tkinter import filedialog
from webbrowser import get
from PIL import Image,ImageTk
from turtle import Screen
from moviepy import*
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil
def select_path():
    path=filedialog.askdirectory()
    L1.config(text=path)


def download_file():
    #pass
    get_link=link_field.get()
    user_path=L1.cget("text")
    Screen.title("Downloading")
    HD_video=YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip=VideoFileClip(HD_video)
    vid_clip.close()
    shutil.move(HD_video,user_path)
    Screen.title("Download complete! Download another file...")
Screen=Tk()
Screen.title("youtube Download")
Canvas=Canvas(Screen,width=500,height=500)
Canvas.pack()
img=Image.open(r"C:\Users\yadaa\Downloads\youtube-logo-png.png")
img=img.resize((250,80),Image.ANTIALIAS)
img32=ImageTk.PhotoImage(img)
Canvas.create_image(273,50,image=img32)
L = Label(Screen,text = "Enter Download link",font=['Arial',15])
link_field=Entry(Screen,width=50)
Canvas.create_window(260,130,window=L)
Canvas.create_window(265,160,window=link_field)
L1 = Label(Screen,text = "Select path for Download",font=['Arial',12])
select_btn=Button(Screen,text="Select",command=select_path)
Canvas.create_window(260,200,window=L1)
Canvas.create_window(265,270,window=select_btn)
btn=Button(Screen,text="Download file",command=download_file)
Canvas.create_window(265,320,window=btn)
Screen.mainloop()
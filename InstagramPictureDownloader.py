# Ahmed Arafat
# Business Information System
# ahmedmoyousry.bis@gmail.com
# 4-2021
# Happy Ramadan <3
import instaloader
from PIL import ImageTk , Image
import tkinter as tk 
from tkinter import messagebox

win = tk.Tk()
win.title("Instagram Profile Picture Downloader By Ahmed Arafat")

def imgDownload():
    Instagram = instaloader.Instaloader()
    profile = entry.get()
    Instagram.download_profile(profile, profile_pic_only = True)
    messagebox.showinfo("Status","Image Downloaded Successfully")

Picture = Image.open("c:/Users/Ahmed Arafat/Desktop/Chillout.jpg")
Picture = Picture.resize((200,200),Image.ANTIALIAS)
resized_img = ImageTk.PhotoImage(Picture)

title = tk.Label(win,text="Instagram Image Downloader",font=("Times",20,"bold"))
title.grid(row=0,column=0,columnspan=5,padx=30,pady=10)

image = tk.Label(win , image = resized_img)
image.grid(row=2,column=0,columnspan=5,pady=20)

LBL = tk.Label(win,text="Enter Username: ",font=("Arial",10))
LBL.grid(row=3,column=0)

entry = tk.Entry(win,width=40)
entry.grid(row=3,column=1,columnspan=3)

btn = tk.Button(win , text=" Download ", command=imgDownload)
btn.grid(row=4,column=0,columnspan=5,pady=10)

win.mainloop()

import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
top=tk.Tk()
top.geometry("500x500")
top.title("Images using PIL library")

def msg():
    label=Label(top,text="Button is clicked")
    label.pack()
image=Image.open("ironman.jpeg").resize((50,50))
tk_image=ImageTk.PhotoImage(image)

image_gif=Image.open("ironman(gif).gif").resize((50,50))
tk_image_gif=ImageTk.PhotoImage(image_gif)

label1=Label(top,image=tk_image_gif)
label1.pack()
button=Button(top,text="button",image=tk_image,command=msg,compound="left")
button.pack()


top.mainloop()

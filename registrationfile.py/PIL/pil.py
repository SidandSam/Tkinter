import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
top=tk.Tk()
top.geometry("500x500")
top.title("Images using PIL library")
image=Image.open("ironman.jpeg").resize((500,500))
tk_image=ImageTk.PhotoImage(image)

label=Label(top,image=tk_image)
label.pack()


top.mainloop()
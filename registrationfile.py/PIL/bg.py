import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
top=tk.Tk()
top.geometry("1920x1080")
top.title("bg image")
image=Image.open("ironman.jpeg").resize((1920,1080))
tk_image=ImageTk.PhotoImage(image)

bg_label=Label(top,image=tk_image)
bg_label.place(relwidth=1,relheight=1)




top.mainloop()
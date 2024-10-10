import tkinter as tk
from tkinter import *

top=tk.Tk()
top.geometry("800x1080")
top.title("keyboard inputs")

def clicker(event):
    label1=Label(top,text="key pressed :"+event.keysym)
    label1.pack()
btn1=Button(top,text="click me")
btn1.pack()
top.bind("<KeyPress>",clicker)


top.mainloop()
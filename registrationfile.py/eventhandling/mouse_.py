import tkinter as tk
from tkinter import *



top=tk.Tk()
top.geometry("300x300")
top.title("mouse_clicks")

def clicker(event):
    label1=Label(top,text="you clicked a button")
    label1.pack()

btn1=Button(top,text="click me")
btn1.bind("<Button-1>",clicker)
btn1.pack()

top.mainloop()
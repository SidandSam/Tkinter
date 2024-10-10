import tkinter as tk
from tkinter import *
top=tk.Tk()
top.geometry("500x500")
top.title("paint app")

can=Canvas(top,width=500,height=500,bg="white")
can.pack(fill="both")

def draw(event):
    x,y=event.x,event.y
    can.create_oval(x-2,y-2,x+2,y+2,fill="black")
can.bind("<B1-Motion>",draw)
top.mainloop()

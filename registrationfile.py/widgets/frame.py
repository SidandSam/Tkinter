import tkinter as tk
from tkinter import *
top=tk.Tk()
top.geometry("300x300")
top.title("frames")
top_frame=Frame(top,bg="Lightblue")
top_frame.pack(side=TOP,fill=BOTH,expand=True)
bottom_frame=Frame(top,bg="Lightgreen")
bottom_frame.pack(side=BOTTOM,fill=BOTH,expand=True)
btn1=Button(top_frame,text="submit")
btn1.pack()
btn2=Button(bottom_frame,text="submit2")
btn2.pack()




top.mainloop()
import tkinter as tk
from tkinter import *
top=tk.Tk()
top.title("Nested Frames")
top.geometry("500x500")
#main frame
main_frame=Frame(top)
main_frame.pack(fill=BOTH,expand=True)
#left frame
left_frame=Frame(main_frame,bg="lightblue")
left_frame.pack(side=LEFT,fill=BOTH,expand=True)
#rightframe
right_frame=Frame(main_frame,bg="lightgreen")
right_frame.pack(side=RIGHT,fill=BOTH,expand=True)
#nested frame
nested=Frame(right_frame,bg="lightgreen")
nested.pack()
#create button
btn1=Button(nested,text="nested frames",bg="red")
btn1.pack()

top.mainloop()
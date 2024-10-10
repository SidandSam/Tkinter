import tkinter as tk
from tkinter import *
top=tk.Tk()

top.title("canvas example")
can=Canvas(top,width=400,height=400,bg="white")
can.pack()
can.create_line(50,50,350,50,fill="blue",width=2)
can.create_rectangle(100,100,300,200,outline="green",width=2)
can.create_oval(150,150,250,250,outline="red",width=2)
can.create_polygon(200,300,250,350,150,350,outline="purple",fill="yellow",width=2)
can.create_text(200,50,text="canvas example",fill="black")
top.mainloop()
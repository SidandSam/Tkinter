#panedwindow:It is a type of widget which acts as a container which allows you to orgainse other widgets.provides adjustable panes between them.

import tkinter as tk
from tkinter import *

top=tk.Tk()
top.geometry("500x500")
top.title("paned window")
#create a panedwindow
panedwindow=PanedWindow(top,orient=HORIZONTAL)
panedwindow.pack(fill=BOTH,expand=1)

#create left and right panes(frames)
left=Frame(panedwindow,bg="Lightblue",width=250,height=500)
right=Frame(panedwindow,bg="green",width=250,height=500)
#add the panes to paned window
panedwindow.add(left)
panedwindow.add(right)

left_label=Label(left,text="LEFT PANE",bg="Lightblue")
left_label.pack()

right_label=Label(right,text="RIGHT PANE",bg="Lightgreen")
right_label.pack()

top.mainloop()
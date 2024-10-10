#toplevel : It is a widget used to create a window(child window) which is addittion to main window(root window)
import tkinter as tk
from tkinter import *

top=tk.Tk()
top.geometry("500x500")
top.title("Main window")
#create a toplevel window
child=Toplevel(top)
child.title("child window")
child.geometry("250x250")
#add a label
label1=Label(child,text="This is a child window")
label1.pack()
top.mainloop()
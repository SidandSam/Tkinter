#grab_set():it creates modal window---we must close child window  before interacting with parent window
import tkinter as tk
from tkinter import *
top=tk.Tk()
top.title("main window")
top.geometry("500x500")
def open_modal():
    child=Toplevel(top)
    child.title("modal window")
    child.geometry("250x250")

    label1=Label(child,text="this is modal  window")
    label1.pack()

    child.transient(top)
    child.grab_set()#prevent interaction with main window until we close the child window
btn1=Button(top,text="open modal window",command=open_modal)
btn1.pack()
top.mainloop()
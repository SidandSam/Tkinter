import tkinter as tk
from tkinter import *
from tkinter import ttk
top=tk.Tk()
top.geometry("800x1080")
top.title("progress bar")
progress=ttk.Progressbar(top,orient="horizontal",length=300,mode="determinate")
progress.pack()

def start_progress():
    progress["value"]=0
    top.update_idletasks()
    for i in range(1,101):
        progress["value"]=i
        top.update_idletasks()
        top.after(50)
start_button=Button(top,text="start download",command=start_progress)
start_button.pack()
top.mainloop()
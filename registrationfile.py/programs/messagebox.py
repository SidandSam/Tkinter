import tkinter as tk
from tkinter import *
from tkinter import messagebox

top=tk.Tk()
top.geometry("500x500")
top.title("messagebox example")
def show_messagebox():
    messagebox.showinfo("information","this is information message")
    messagebox.showwarning("warning","this is warning message")
    messagebox.showerror("error","this is error message")
    response=messagebox.askquestion("question","do you like tkinter")
    if response=="yes":
        print("user likes tkinter")
    else:
        print("user doesnt like tkinter")
        
    if messagebox.askyesno("yes/no","are you sure"):
        print("user clicked yes")
    else:
        print("user clicked no")
    if messagebox.askretrycancel("retry","do you want to retry?"):
        print("user clicked retry")
    else:
        print("user clicked cancel")
btn1=Button(top,text="click",command=show_messagebox)
btn1.pack()
    
        
top.mainloop()
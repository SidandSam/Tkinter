import tkinter as tk
from tkinter import *
from tkinter import messagebox
import subprocess

top=tk.Tk()
top.title("login")
top.geometry("500x500")

def login():
    username=user_entry.get()
    password=pass_entry.get()
    if username=="sid" and password=="sam":
        messagebox.showinfo("Login successful","Welcome to food app")
        top.destroy()
        subprocess.Popen(['python','foodapp.py'])
    else:
        messagebox.showerror("Login Failed","Invalid Details")
        
    
user_label=Label(top,text="User Name:")
user_label.grid(row=0,column=0)
user_entry=Entry(top)
user_entry.grid(row=0,column=1)

pass_label=Label(top,text="Password:")
pass_label.grid(row=1,column=0)
pass_entry=Entry(top)
pass_entry.grid(row=1,column=1)
login_button=Button(top,text="login",command=login)
login_button.grid(row=2,column=2)
top.mainloop()
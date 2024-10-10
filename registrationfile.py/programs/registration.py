import tkinter as tk
from tkinter import messagebox
from tkinter import Radiobutton
top=tk.Tk()
top.geometry("800x800")
top.title("registration form")
var=tk.IntVar()


def submit_form():
    #get the values from entries
    first_name=entry_fn.get()
    last_name=entry_ln.get()
    email=entry_em.get()
    password=entry_ps.get()
    gender=var.get()
    agreed=var1.get()

    if not first_name or not last_name or not email or not gender or not password:
        messagebox.showwarning("ALL FIELDS ARE REQUIRED!")
        return
    messagebox.showinfo("Registration Successful",f"First Name:{first_name}\nLast Name:{last_name}\nEmail:{email}\nPassword:{password},Gender:{gender}")


Label1=tk.Label(top,text="first name:",fg="red",bg="yellow",font=("TImes New Roman",15))
Label2=tk.Label(top,text="last name:",fg="blue",bg="green",font=("TImes New Roman",15))
Label3=tk.Label(top,text="email:",bg="black",fg="white",font=("TImes New Roman",15))
Label4=tk.Label(top,text="password:",bg="purple",fg="pink",font=("TImes New Roman",15))
Label5=tk.Label(top,text="gender:",bg="brown",fg="grey",font=("TImes New Roman",15))

entry_fn=tk.Entry(top)
entry_ln=tk.Entry(top)
entry_em=tk.Entry(top)
entry_ps=tk.Entry(top,show="*")

rad1=Radiobutton(top,text="male",variable=var,value="1")
rad2=Radiobutton(top,text="female",variable=var,value="2")
rad3=Radiobutton(top,text="other",variable=var,value="3")
sub=tk.Button(top,text="submit",command=submit_form)

var1=tk.BooleanVar()
check=tk.Checkbutton(top,text="I have agreed with all terms and conditions",variable=var1)


Label1.grid(row=0,column=0,pady=1)
entry_fn.grid(row=0,column=1)
Label2.grid(row=1,column=0)
entry_ln.grid(row=1,column=1)
Label3.grid(row=2,column=0)
entry_em.grid(row=2,column=1)
Label4.grid(row=3,column=0)
entry_ps.grid(row=3,column=1)
Label5.grid(row=4,column=0)
rad1.grid(row=4,column=1)
rad2.grid(row=4,column=2)
rad3.grid(row=4,column=6)
check.grid(row=5,column=2)
sub.grid(row=6,column=2)

top.mainloop()

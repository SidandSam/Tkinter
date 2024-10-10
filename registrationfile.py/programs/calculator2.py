import tkinter as tk
from tkinter import *

top=tk.Tk()
top.geometry("750x750")
top.title("calculator ")
equation=''
def clear():
    global equation
    equation=''
    label_result.config(text=equation)

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)
    
def calculate():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="Error"
            equation=""
    label_result.config(text=result)
    
label_result=Label(top,text=" ",height=2,width=25,font=("arial",30))
label_result.pack()

Button(top,text="C",height=1,width=5,font=("arial",30,"bold"),command=lambda:clear()).place(x=10,y=100)
Button(top,text="/",height=1,width=5,font=("arial",30,"bold"),command=lambda:show("/")).place(x=150,y=100)
Button(top,text="%",height=1,width=5,font=("arial",30,"bold"),command=lambda:show("%")).place(x=290,y=100)

Button(top,text="7",height=1,width=5,font=("arial",30,"bold"),command=lambda:show("7")).place(x=10,y=200)
Button(top,text="8",height=1,width=5,font=("arial",30,"bold"),command=lambda:show("8")).place(x=150,y=200)
Button(top,text="9",height=1,width=5,font=("arial",30,"bold"),command=lambda:show("9")).place(x=290,y=200)

Button(top,text="*",height=1,width=5,font=("arial",30,"bold"),command=lambda:show("*")).place(x=430,y=200)

Button(top,text="4",height=1,width=5,font=("arial",30,"bold"),command=lambda:show("4")).place(x=10,y=300)
Button(top,text="5",height=1,width=5,font=("arial",30,"bold"),command=lambda:show("5")).place(x=150,y=300)
Button(top,text="6",height=1,width=5,font=("arial",30,"bold"),command=lambda:show("6")).place(x=290,y=300)

Button(top,text="-",height=1,width=5,font=("arial",30,"bold"),command=lambda:show("-")).place(x=430,y=300)

Button(top,text="1",height=1,width=5,font=("arial",30,"bold"),command=lambda:show("1")).place(x=10,y=400)
Button(top,text="2",height=1,width=5,font=("arial",30,"bold"),command=lambda:show("2")).place(x=150,y=400)
Button(top,text="3",height=1,width=5,font=("arial",30,"bold"),command=lambda:show("3")).place(x=290,y=400)

Button(top,text="+",height=1,width=5,font=("arial",30,"bold"),command=lambda:show("+")).place(x=430,y=400)

Button(top,text="0",height=1,width=13,font=("arial",30,"bold"),command=lambda:show("0")).place(x=10,y=500)
Button(top,text=".",height=1,width=5,font=("arial",30,"bold"),command=lambda:show(".")).place(x=290,y=500)
Button(top,text="=",height=1,width=5,font=("arial",30,"bold"),command=lambda:calculate()).place(x=430,y=500)

top.mainloop()

import tkinter as tk
from tkinter import *
import random

top=tk.Tk()
top.geometry("500x500")
top.title("color game")
colors=["red","blue","green","yellow","purple","pink","black","white","orange","brown"]
score=0
timeleft=30
paused=False
def startgame(event):
    if timeleft==30 and not paused:
        countdown()
    if not paused:
        nextcolour()
    
def nextcolour():
    global score
    global timeleft
    if timeleft>0 and not paused:
        answer_entry.focus_set()
        if answer_entry.get().lower()==colors[1].lower():
            score+=1
        answer_entry.delete(0,END)
        random.shuffle(colors)
        color_display.config(fg=str(colors[1]),text=str(colors[0]))
        score_label.config(text="Score:"+str(score))

def countdown():
    global timeleft
    if timeleft>0 and not paused:
        timeleft-=1
        timer_label.config(text="Time left:"+str(timeleft))
        timer_label.after(1000,countdown)
    elif timeleft==0:
        final_score()
def final_score():
    final_score_window=Toplevel(top)
    final_score_window.title("Final Score")
    final_score_window.geometry("250x250")
    final_label=Label(final_score_window,text=f"Your final score is {score}",font={"Helvetica",30})
    final_label.pack()
    restart_button=Button(final_score_window,text="play again",command=restart)
    restart_button.pack()
    final_score_window.grab_set()

def restart():
    global timeleft,score
    timeleft=30
    score=0
    paused=False
    score_label.config(text="press enter to start")
    timer_label.config(text="Time Left:"+str(timeleft))
    color_display.config(text="",fg="black")
    answer_entry.delete(0,END)

def pause():
    global paused
    if paused:
        paused=False
        pause_button.config(text="pause")
        countdown()
        nextcolour()
    else:
        paused=True
        pause_button.config(text="Resume")
    
instruction=Label(top,text="•type the color of the word and not the text")
instruction.pack()
pause_button=Button(top,text="Pause",command=pause)
pause_button.pack()
score_label=Label(top,text="press enter to start")
score_label.pack()
restart_button=Button(top,text="play again",command=restart)
restart_button.pack()
timer_label=Label(top,text="TIME LEFT:"+str(timeleft))
timer_label.pack()
color_display=Label(top,font=("Helvetica",60))
color_display.pack()
answer_entry=Entry(top)
top.bind('<Return>',startgame)
answer_entry.pack()
answer_entry.focus_set()
top.mainloop()

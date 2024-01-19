from tkinter import *

#------------constants------------------------------

PINK="#e2979c"
RED="#e7385b"
GREEN="#9bdeac"
WORK_MIN=60
SHORT_BREAK_MIN=5
LONG_BREAK_MIN=20
reps=0
timer=None

#---------------------------------------------------
import time
import math


def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="WELCOME")
    global reps
    reps=0
    star_button["state"] = "normal"

def count_down(count):

    count_min=math.floor(count/60)
    count_sec=count % 60

    if count_sec<10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer= window.after(1000,count_down,count-1)
    else:
        star_time()
        #reps

def star_time():
    global reps
    reps+=1
    star_button["state"] = "disabled"
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN * 60
    long_break_sec=LONG_BREAK_MIN * 60

    if  reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="BREAK", fg=RED)

    elif reps % 2 == 0:
          count_down(short_break_sec)
          title_label.config(text="BREAK", fg=RED)

    else:
        count_down(work_sec)
        title_label.config(text="WORK", fg=RED)


#--------------------------------------------------

window=Tk()
window.title("WORK")
window.minsize(width=500,height=500)
window.config(padx=100,pady=100,bg="white")

title_label=Label(text="WELCOME",fg="black",bg="white",font="bold")
title_label.grid(column=1,row=0)

canvas=Canvas(width=200,height=220,bg=RED,highlightthickness=0)
tomate_img= PhotoImage(file="im.png")
canvas.create_image(100,112,image=tomate_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font="bold")
canvas.grid(column=1,row=1)
#canvas.pack()

star_button=Button(text="Start",highlightthickness=0,command=star_time)
star_button.grid(column=0,row=2)

reset_button=Button(text="Reset",highlightthickness=0,command=reset_time)
reset_button.grid(column=2,row=2)

window.mainloop()

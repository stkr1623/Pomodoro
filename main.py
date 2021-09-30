from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    my_label.config(text="Timer",font=(FONT_NAME,35,"bold"),fg='#6ECB63',bg = "#664E88")
    canvas.itemconfig(timer_text,text='25:00')
    check_marks.config(text="",fg='#6ECB63',bg = "#3B0000",font=(FONT_NAME,10,"bold"))
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        my_label.config(text="LBreak",font=(FONT_NAME,35,"bold"),fg='#FF0000',bg = "#664E88")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        my_label.config(text="SBreak",font=(FONT_NAME,35,"bold"),fg='#FF0000',bg = "#664E88")

    else:
        count_down(WORK_MIN * 60)
        my_label.config(text="work ", font=(FONT_NAME, 35, "bold"), fg='#FFB740', bg="#664E88")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time

def count_down(count):
    count_min=math.floor(count/60)
    count_sec= count %60
    if count_sec <10:
        count_sec=f'0{count_sec}'
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        global mark
        mark= ""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            mark+="✔"
        check_marks.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Game")
window.config(padx=50,pady=50,bg = "#664E88")
window.minsize(width=400,height=400)


my_label=Label(text="Timer",font=(FONT_NAME,35,"bold"),fg='#6ECB63',bg = "#664E88")
my_label.grid(column=1,row=0)

canvas = Canvas(width=200,height=224,bg = "#664E88", highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(101,112,image=tomato_img)
timer_text=canvas.create_text(103,112,text="25:00",font=(FONT_NAME,25,"bold"),fill="white")

canvas.grid(column=1,row=1)


Start_button=Button(text="Start",bg='#FFB319',font=(FONT_NAME,10,"bold"),command=start_timer)
Start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",bg='#FFB319',font=(FONT_NAME,10,"bold"),command= reset)
reset_button.grid(column=2,row=2)

check_marks= Label(fg='#6ECB63',bg = "#3B0000",font=(FONT_NAME,10,"bold"))
check_marks.grid(column=1,row=2)
name_label=Label(text="Designed by Tharun ",font=(FONT_NAME,10,"bold"),pady=5)
name_label.grid(column=1,row=3)
window.mainloop()
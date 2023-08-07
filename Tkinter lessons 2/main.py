from tkinter import*
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✓"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="TIMER")
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, CHECK_MARK
    reps += 1
    if reps % 2 == 1:
        count_down(WORK_MIN * 60)
        title.config(text="WORK", fg=GREEN)
    elif reps % 4 == 0:
        CHECK_MARK += "✓"
        count_down(LONG_BREAK_MIN * 60)
        title.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 5)
        title.config(text="BREAK", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    global reps, WORK_MIN, timer
    if seconds >= 60:
        WORK_MIN = floor(seconds / 60)
        seconds %= 60
    show_seconds = floor(seconds)
    if seconds == 60:
        show_seconds *= 0
    if len(str(show_seconds)) > 1:
        canvas.itemconfig(timer_text, text=f"{WORK_MIN}:{show_seconds}")
    else:
        canvas.itemconfig(timer_text, text=f"{WORK_MIN}:0{show_seconds}")
    if seconds > 0:
        timer = window.after(1000, count_down, seconds-1)
    else:
        seconds += 60
        WORK_MIN -= 1
        timer = window.after(1000, count_down, seconds-1)
    if WORK_MIN <= 0:
        reps += 1
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(bg=YELLOW, padx=90, pady=40)

title = Label(text="TIMER", font=(FONT_NAME, 35, "normal"), fg=GREEN, bg=YELLOW)
title.pack()

canvas = Canvas()
canvas.config(bg=YELLOW, height=224, width=205, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_img)
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

start_button = Button(text="START", highlightthickness=0, command=start_timer)
start_button.pack(side="left")
reset_button = Button(text="RESET",command=timer_reset)
reset_button.pack(side="right")

pomodoro_count = Label(text=CHECK_MARK, fg=GREEN, bg=YELLOW)
pomodoro_count.pack(side="bottom")

window.mainloop()

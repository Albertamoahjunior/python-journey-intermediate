from tkinter import*
from questions import Question

FONT = ("Chaucer", 24, "italic")

q = Question()
score = 0


def next_question():
    score_board.config(text=f"Score: {score}", bg="midnightblue", fg="white")
    canvas.config(bg="white")
    canvas.itemconfig(question, text=q.next_question(score))


def check_true():
    global score
    if q.answer == "True":
        canvas.config(bg="#31f47a")
        score += 1
    else:
        canvas.config(bg="#df1d4b")
    window.after(ms=2000, func=next_question)

def check_false():
    global score
    if q.answer == "False":
        canvas.config(bg="#31f47a")
        score += 1
    else:
        canvas.config(bg="#df1d4b")
    window.after(ms=2000, func=next_question)


window = Tk()
window.title("Quizzer App")
window.config(height=500, width=300, bg="midnightblue")
window.after(60)

score_board = Label()
score_board.config(text=f"Score: {score}", bg="midnightblue", fg="white")
score_board.grid(column=1, row=0)

canvas = Canvas()
question = canvas.create_text(140, 150, text=q.get_question(), width=280, font=FONT)
canvas.config(height=300, width=280, bg="white")
canvas.grid(column=0, row=1, columnspan=2, padx=50, pady=20)



false = PhotoImage(file="false.png")
true = PhotoImage(file="true.png")
true_button = Button()
true_button.config(bg="red", image=false, command=check_true)
true_button.grid(column=1, row=2, pady=20)
false_button = Button()
false_button.config(bg="green", image=true, command=check_false)
false_button.grid(column=0, row=2, pady=20)


window.mainloop()
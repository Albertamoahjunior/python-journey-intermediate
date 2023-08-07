from tkinter import*
import pandas
import random

translation_list = ["English"]
word_list = ["French"]
save_word={}
play = False
try:
    words = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    words = pandas.read_csv("french_words.csv")
    words_to_learn = {
        "French": word_list,
        "English": translation_list
    }
    headers = pandas.DataFrame.from_dict(words_to_learn)
    headers.to_csv("words_to_learn.csv", header=False, sep=",", index=False, mode='w')


keys = []
for key in words:
    keys.append(key)
language = keys[0]

language_word ={
    keys[0]: [words[keys[0]]],
    keys[1]: [words[keys[1]]]
}
word = random.choice(language_word[keys[0]][0])

def show_translation():
    global word
    translation = language_word[keys[0]][0].to_list()
    translation = translation.index(word)
    translation = language_word[keys[1]][0][translation]
    canvas.create_image(450, 300, image=image_back)
    canvas.create_text(450, 200, text=keys[1], font=("courier", 24, "normal"), fill="white")
    canvas.create_text(450, 250, text=translation, font=("Arial", 24, "bold"), fill="white")
    print(translation)
    return translation

def next_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(language_word[keys[0]][0])
    canvas.create_image(450, 300, image=image_front)
    language = keys[0]
    canvas.create_text(450, 200, text=language, font=("courier", 24, "normal"))
    canvas.create_text(450, 250, text=word, font=("courier", 24, "bold"))
    flip_timer = window.after(3000, func=show_translation)

def check_wrong():
   global word, translation_list, word_list, save_word
   translation = language_word[keys[0]][0].to_list()
   translation = translation.index(word)
   word_list[0] = word
   translation_list[0] = language_word[keys[1]][0][translation]
   save_word = {
       keys[0]: word_list,
       keys[1]: translation_list,
   }
   next_word()
   word_for_learn = pandas.DataFrame.from_dict(save_word)
   word_for_learn.to_csv("words_to_learn.csv", header=False, sep=",", index=False, mode='a')
   print(save_word)


def check_right():
   language_word[keys[0]][0].to_list().remove(word)
   language_word[keys[1]][0].to_list().remove(show_translation())
   next_word()

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(width=800, height=600, bg=BACKGROUND_COLOR)

flip_timer =window.after(3000, func=show_translation)

image_front = PhotoImage(file="card_front.png")
image_back = PhotoImage(file="card_back.png")
image_wrong = PhotoImage(file="wrong.png")
image_right = PhotoImage(file="right.png")

canvas = Canvas(height=570, width=900, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(450, 300, image=image_front)
canvas.create_text(450, 200, text=language, font=("courier", 24, "normal"))
canvas.create_text(450, 250, text=word, font=("courier", 24, "normal"))
canvas.grid(column=0, row=0, columnspan=2)

wrong = Button(image=image_wrong, highlightthickness=0, borderwidth=0, command=check_wrong)
wrong.grid(row=1, column=0)
wrong = Button(image=image_right, highlightthickness=0, borderwidth=0, command=check_right)
wrong.grid(row=1, column=1)


window.mainloop()
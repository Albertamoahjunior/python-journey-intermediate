import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_got_clicked():
    response = input.get()
    label["text"] = response

#labels
label = tkinter.Label(text= "New Text")
label["bg"] = "red"
label["fg"] = "white"
label.grid(column=0, row=0)

#buttons
button = tkinter.Button(command=button_got_clicked)
button["bg"] = "red"
button["text"] = "exit"
button.grid(column=1, row=1)

#Entry
input = tkinter.Entry(width=20)
input.grid(column=3, row=2)

button2 = tkinter.Button(command=button_got_clicked)
button2["bg"] = "red"
button2["text"] = "new button"
button2.grid(column=2, row=0)

# #text
# text = tkinter.Text(width=20, height=10)
# text.focus()
# text.pack()
#
# #spinbox
# spinbox = tkinter.Spinbox(from_=0, to= 10)
# spinbox.pack()
#
# #check box
# def check_used():
#     print(checked_state.get())
#
# checked_state = tkinter.IntVar()
# check_button = tkinter.Checkbutton(text="is on", variable=checked_state, command=check_used)
# checked_state.get()
# check_button.pack(side="right")


window.mainloop()


from tkinter import*

window = Tk()
window.title("Mile to kilometre Converter")
window.minsize(width=350, height=300)
window.config(pady=90, padx=85)


def convert():
    to_convert = mile_input.get()
    converted = int(to_convert) * 1.6
    answer_panel["text"] = str(converted)


answer = Label(text="is equal to: ")
answer.grid(column=0, row=1)

mile_input = Entry(width=10)
mile_input.focus()
mile_input.grid(column=1, row=0)

answer_panel = Label(text=" 0 ")
answer_panel.grid(column=1, row=1)

kilometre_unit = Label(text=" km ")
kilometre_unit.grid(column=2, row=1)

mile_unit = Label(text=" Miles ")
mile_unit.grid(column=2, row=0)

calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()

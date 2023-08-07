from tkinter import*
from tkinter import messagebox
import random
import pyperclip
import json
# ------------------------------------------------------------------------------- #
def find_info():
    try:
        with open("Passwords.json", "r") as read_file:
            content = json.load(read_file)
    except FileNotFoundError:
        messagebox.showinfo("OOPS", message="No data saved yet")
    else:
        try:
            email = ""
            data_pass = " "
            for info in content:
                if info == website.get():
                    email = content[info]
                    data_pass = content[info]
                    email = email['email']
                    data_pass = data_pass['password']
        except KeyError:
            messagebox.showinfo("OOPS", message="No such info exists")
        else:
            messagebox.showinfo(website.get(), message=f"Email: {email}\n password: {data_pass}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 14)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    letters_picked = []
    for n in range(0, int(nr_letters)):
        position = random.randint(0, len(letters) - 1)
        letters_picked.append(letters[position])

    numbers_picked = []
    for n in range(0, int(nr_numbers)):
        position = random.randint(0, len(numbers) - 1)
        numbers_picked.append(numbers[position])

    symbols_picked = []
    for n in range(0, int(nr_symbols)):
        position = random.randint(0, len(symbols) - 1)
        symbols_picked.append(symbols[position])

    passwordGenerated = letters_picked + numbers_picked + symbols_picked
    random.shuffle(passwordGenerated)
    password_use = ""

    for n in range(0, len(passwordGenerated)):
        password_use += passwordGenerated[n]

    password.insert(0, password_use)
    pyperclip.copy(password_use)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    name = username.get()
    web = website.get()
    passkey = password.get()

    data = {
        web: {
            "email": name,
            "password": passkey,
        }
    }
    if len(name) == 0 or len(web) == 0 or len(passkey) == 0:
        messagebox.showinfo(title="OOPS", message="Please do not leave any field empty")
    else:
        go_ahead = messagebox.askokcancel(title=web, message=f"These are the details entered:\nEmail: {name}"
                                                                f"\nPassword: {passkey}\nIs it okay save?")

        if go_ahead:
            try:
                with open("Passwords.json", "r") as data_file:
                    new_data = json.load(data_file)
            except FileNotFoundError:
                with open("Passwords.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            else:
                new_data.update(data)
                with open("Passwords.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            finally:
                    website.delete(0, END)
                    password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(height=400, width=500, pady=20, padx=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = Entry()
website.focus()
website.config(width=32)
website.grid(column=1, row=1)
username = Entry()
username.config(width=50)
username.insert(0, "albertamoah2000@gmail.com")
username.grid(column=1, row=2, columnspan=2, pady=2)
password = Entry()
password.config(width=32)
password.grid(column=1, row=3)

website_name = Label(text="Website:")
website_name.grid(column=0, row=1)
user_name = Label(text="Email/Username:")
user_name.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.config(padx=0)
pass_label.grid(column=0, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
search_button = Button(text="Search", command=find_info, width=13)
search_button.grid(column=2, row=1)
add_button = Button(text="Add")
add_button.config(width=43, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, pady=2)

window.mainloop()

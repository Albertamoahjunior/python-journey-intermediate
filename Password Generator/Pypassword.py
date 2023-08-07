import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Pypassword Generator")

nr_letters = random.randint(8,14)
nr_numbers = random.randint(2, 4)
nr_symbols =random.randint(2, 4)

i = 0
letters_picked = []
for n in range(0, int(nr_letters)):
    position = random.randint(0, len(letters)-1)
    letters_picked.append(letters[position])

numbers_picked = []
for n in range(0, int(nr_numbers)):
    position = random.randint(0, len(numbers)-1)
    numbers_picked.append(numbers[position])

symbols_picked = []
for n in range(0, int(nr_symbols)):
    position = random.randint(0, len(symbols)-1)
    symbols_picked.append(symbols[position])

passwordGenerated = letters_picked + numbers_picked + symbols_picked
random.shuffle(passwordGenerated)
password = ""

for n in range(0, len(passwordGenerated)):
    password += passwordGenerated[n]

print(f"Here is your password: {password}")

with open("../letters/Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.read()

names = names.split("\n")
with open("../letters/Input/Letters/starting_names.txt", "r") as letters_file:
    letter = letters_file.read().split("\n")

for name in names:
    letter[0] = f"Dear {name},"
    with open(f"../letters/Output/ReadToSend/letter_for_{name}.txt", "w") as file:
        file.write("\n".join(letter))

import pandas
nato_phonetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")
codes = nato_phonetic_data.code.to_list()
phonetic_dict = {code[0]: code for code in codes}

def generate_nato_code():
    name = input("Enter a word: ")
    try:
        name_list = [phonetic_dict[letter.upper()] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_nato_code()
    else:
        print(name_list)

generate_nato_code()


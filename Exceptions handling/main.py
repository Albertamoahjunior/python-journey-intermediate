# try:
#     file = open("a_file.txt")
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("I am done")


height = float(input("Enter your height: "))
weight = int(input("Enter your weight: "))


if height > 3:
    raise ValueError("Human height should not be over 3m")

bmi = weight/height**2
print(bmi)
# #first list comprehension exercise
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# with open("file1.txt", "r") as file:
#     file1_numbers = file.readlines()
# with open("file2.txt", "r") as file:
#     file2_numbers = file.readlines()
#
# # squared_numbers = [number**2 for number in numbers]
# # even_numbers = [number for number in numbers if number % 2 == 0]
# #
# # print(squared_numbers)
# # print(even_numbers)
# result = [int(number) for number in file1_numbers if number in file2_numbers]

#print(result)
#
# sentence = "What is the Airspeed velocity of an unladen swallow"
# sentence = sentence.split(" ")
# result = {word: len(word) for word in sentence}
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day: (temp*9/5) + 32 for (day, temp) in weather_c.items()}
# print(weather_f)



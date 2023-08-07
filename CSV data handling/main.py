# # import csv
# # with open("weather_data.csv", "r") as file:
# #     data = csv.reader(file)
# #     temperatures =[]
# #     for row in data:
# #         if "temp" not in row:
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
# #data = pandas.read_csv("weather_data.csv")
#
# # temperatures = data["temp"].to_list()
# # average_temperature = sum(temperatures)/len(temperatures)
#
# # print(data["temp"].mean())
# # print(data["temp"].max())
# #
# # #Get data in columns
# # #print(data["condition"])
# # #print(data.condition)
# #
# # #Get data from rows
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
# #
# # #Get a column from a row
# # monday = data[data.day == "Monday"]
# # print(monday.condition)
# #
# # #manipulate data in rows
# # monday_temp = int(monday.temp)
# # monday_temp = monday_temp*9/5 + 32
# # monday_temp = str(monday_temp)+" F"
# # print(monday_temp)
#
# #create data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# #print(data)
#
# #creation of csv files
# data.to_csv("class_data.csv")

import pandas
data = pandas.read_csv("squirrel_data.csv")
shortlist_color_list =[]
color_squirrels = []
cinnamon_squirrels = 0
grey_squirrels = 0
black_squirrels = 0

#Extracting the various fur colors for the squirrels
color_list = data["Primary Fur Color"].to_list()
for color in color_list:
    if color in shortlist_color_list or color == "nan":
        pass
    else:
        shortlist_color_list.append(color)

#counting the squirrels per color
for color in data["Primary Fur Color"].to_list():
    if color == "Cinnamon":
        cinnamon_squirrels += 1
    elif color == "Gray":
        grey_squirrels += 1
    elif color == "Black":
        black_squirrels += 1


color_squirrels.append(cinnamon_squirrels)
color_squirrels.append(grey_squirrels)
color_squirrels.append(black_squirrels)

#taking out the color nan
shortlist_color_list.pop(0)

#making a squirrel dictionary
squirrel_dict = {
    "Fur Color": shortlist_color_list,
    "Count": color_squirrels
}

#converting squirrel dictionary to a dataframe

squirrel_count = pandas.DataFrame(squirrel_dict)


#creating a csv file from the data frame
squirrel_count.to_csv("squirrel_count.csv")
# print(shortlist_color_list)
# print(color_squirrels)

# fruits = ["Apple", "Pear", "Orange"]
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("fruit pie")
#     else:
#         print(fruit + " pie")
#     finally:
#         print("making is done")
#
# fruit_number = int(input("Enter the index of your fruit beginning from 0: "))
#
# make_pie(fruit_number)

facebook_posts =[
    {'likes': 21, 'Comments': 2},
    {'likes': 13, 'Comments': 2, 'Shares': 1},
    {'likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'likes': 19, 'Comments': 3}
]

total_likes = 0
for post in facebook_posts:
    try:
        total_likes += post['likes']
    except KeyError:
        total_likes += 0


print(total_likes)
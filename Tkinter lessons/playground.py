# def calculate(**kwargs):
#     answer = 0
#     answer += kwargs["add"]
#     answer *= kwargs["multiply"]
#     answer -= kwargs["subtract"]
#     answer /= kwargs["divide"]
#     return answer
#
# print(calculate(add= 4, multiply = 2, subtract = 0, divide = 1))

check = input("Enter the numbers: ")
answer = 0
parameter_list =[]
for n in check:
    parameter_list.append(n)

print(parameter_list)

for n in parameter_list:
    count = 0
    if n == "+":
        answer = int(parameter_list[parameter_list.index(n) - 1]) + int(parameter_list[parameter_list.index(n) + 1])
        # if count > 0:
        #     pass
        # else:
        #     answer = int(parameter_list[parameter_list.index(n)-1]) + int(parameter_list[parameter_list.index(n)+1])

    #count += 1

print(answer)



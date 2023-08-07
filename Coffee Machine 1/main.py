from coffee_data import coffee_flavours
from coffee_data import coffee_tank

buy = True

def print_report():
    water = "water"
    milk = "milk"
    coffee = "coffee"
    money = "money"
    print(f"Water: {coffee_tank[water]}ml")
    print(f"Milk: {coffee_tank[milk]}ml")
    print(f"Coffee: {coffee_tank[coffee]}ml")
    print(f"Money: ${coffee_tank[money]}")


def update_resource(coffee):
    for resource in coffee_flavours[coffee]:
        if resource != "price":
            coffee_tank[resource] -= coffee_flavours[coffee][resource]
        else:
            coffee_tank["money"] += coffee_flavours[coffee][resource]



def calculate_user_money(penny, dime, nickel, quarter):
    user_money = penny + dime + nickel + quarter
    return int(user_money)


def check_resource(coffee, user_money):
    short_resources = ""
    if user_money < coffee_flavours[coffee]["price"]:
        print("Your money is not sufficient")
    else:
        for resource in coffee_flavours[coffee]:
            if resource != "price":
                if coffee_flavours[coffee][resource] > coffee_tank[resource]:
                    short_resources += f", {resource}"
            if len(short_resources) >= 1:
                print(f"Sorry there is not enough {short_resources}")
                return False
            else:
                if user_money != coffee_flavours[coffee]["price"]:
                    change = user_money - coffee_flavours[coffee]["price"]
                    change /= 100
                    print(f"You have a change of ${change}")
                return True


def buy_coffee(coffee):
    print(f"Here is your {coffee}")
    update_resource(coffee)

while buy:
    want = input("What would you like? (espresso/latte/cappuccino/report):")
    if want == "report":
        print_report()
    else:
        print("Please insert coins: ")
        quarter = input("How many quarters: ")
        dime = input("How many dimes: ")
        nickel = input("How many nickels: ")
        penny = input("How many pennies: ")

        user_money = calculate_user_money(penny, dime, nickel, quarter)
        buy = check_resource(want, user_money)
        if buy:
            buy_coffee(want)









from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
#menu_item = MenuItem()
is_on = True

def print_report():
    coffee_maker.report()
    money_machine.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like?:({options}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            payment = money_machine.make_payment(drink.cost)
            payment
            if payment:
                coffee_maker.make_coffee(drink)




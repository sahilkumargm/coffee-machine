from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

def make_coffee():
    print("Welcome! What would you like? ")
    user_input = input(coffee_menu.get_items())
    print(f"You have ordered a {user_input}")

    # find the drink in the menu and show them the price of the coffee
    choice_of_coffee = coffee_menu.find_drink(user_input.lower())
    print(f"Cost of your coffee is: {choice_of_coffee.cost}")

    # check if there are enough resources to make the coffee
    # if there is, get ready to make the coffee,

    is_ready = False
    if coffee_maker.is_resource_sufficient(choice_of_coffee):
        is_ready = True
        print("READY..")

    # Enter coins
    if money_machine.make_payment(choice_of_coffee.cost) and is_ready:
        coffee_maker.make_coffee(choice_of_coffee)
        print("Done")


flag = True
while flag is True:
    to_dispense = input("Press 'A' to dispense coffee or '0' to generate report ")
    if to_dispense == '0':
        money_machine.report()
        coffee_maker.report()
    elif to_dispense == "a".lower():
        make_coffee()
    elif to_dispense == "Shutdown".lower():
        print("Goodbye")
        flag = False
    else:
        print("Invalid option. Please try again.")



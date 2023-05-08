from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

in_use = True

while in_use:
    options = menu.get_items()
    user_choice = input(f"What would you like? {options}: ").lower()
    if user_choice == "off":
        print("I am turning off....")
        in_use = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(coffee):
            price = coffee.cost
            if money_machine.make_payment(price):
                coffee_maker.make_coffee(coffee)






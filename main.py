from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#
# make = CoffeeMaker()
# menu = Menu()
# # item = MenuItem()
# money_machine = MoneyMachine()
#
# drink = input(f"Please choose a drink! ({menu.get_items()}): ").lower()
#
# '''Makes Report'''
# make.report()
# money_machine.report()
#
# """resources sufficeint or not"""
#
# choice = menu.find_drink(drink)
# print(make.is_resource_sufficient(choice))
#
#
# '''Process Money'''
#
# money_machine.process_coins()
#
#
# '''Check transaction successful'''
#
#
#
#
# '''Make Coffee'''



money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to drink? ({options}): ").lower()
    if choice == 'off':
        is_on = False
        print("Have a nice day! :)")
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients  and is_payment_successful:
            coffee_maker.make_coffee(drink)



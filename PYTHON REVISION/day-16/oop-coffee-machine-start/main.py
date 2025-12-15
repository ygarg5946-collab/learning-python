from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
menu=Menu()
coffee_maker=CoffeeMaker()
# first task is to print the report
coffee_maker.report()
money_machine.report()
# the second thing is to check the availability of the resources
is_on=True
while is_on:
    options=menu.get_items()
    choice=input(f"Which coffee would you like? ({options}) ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


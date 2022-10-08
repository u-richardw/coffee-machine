import money_machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

machine_on = True


while machine_on:
    options = menu.get_items()
    order = input(f"What would you like? ({options}): ")
    if order == "off":
        machine_on = False
        print("Machine is off")
    elif order == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(order)
        if coffee.is_resource_sufficient(drink):
            if(money.make_payment(drink.cost)):
                coffee.make_coffee(drink)
        else:
            print("Not enough resources")




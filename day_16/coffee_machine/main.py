from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

def start():

    user_input = input(f"What would you like? ({menu.get_items()}): ")
    while user_input != "off":
        if user_input == "report":
            coffee_machine.report()
        else:
            drink = menu.find_drink(user_input)
            if (drink and
                    coffee_machine.is_resource_sufficient(drink) and
                    money_machine.make_payment(drink.cost)):
                coffee_machine.make_coffee(drink)

        user_input = input(f"What would you like? ({menu.get_items()}): ")


start()

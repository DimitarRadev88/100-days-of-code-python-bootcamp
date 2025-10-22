from day_16.coffee_machine.menu import MenuItem


class CoffeeMaker:
    resources: dict

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        print(f"Water: {self.resources["water"]}ml")
        print(f"Milk: {self.resources["milk"]}ml")
        print(f"Coffee: {self.resources["coffee"]}g")

    def is_resource_sufficient(self, drink: MenuItem):
        for ingredient in drink.ingredients.keys():
            if self.resources[ingredient] < drink.ingredients[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                return False

        return True

    def make_coffee(self, order: MenuItem):
        for ingredient in order.ingredients.keys():
            self.resources[ingredient] -= order.ingredients[ingredient]
        print(f"Here is your {order.name} ☕️. Enjoy!")

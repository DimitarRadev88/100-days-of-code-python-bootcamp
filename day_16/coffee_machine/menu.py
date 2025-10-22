class MenuItem:
    name: str
    cost: float
    ingredients: dict

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    items: list[MenuItem]

    def __init__(self):
        self.items = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        result = ""
        for item in self.items:
            result += item.name + "/"
        return result

    def find_drink(self, order_name: str):
        for item in self.items:
            if item.name == order_name:
                return item

        print("Sorry that item is not available.")
        return None

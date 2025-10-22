from prettytable import PrettyTable, TableStyle

table = PrettyTable()

pokemon = {
    "Pikachu": "Electric",
    "Froaki": "Water ",
    "Pyroar": "Fire"
}

table.add_column("Pokemon Name", list(pokemon.keys()))
table.add_column("Type", list(pokemon.values()))

table.__setattr__("align", "l")
table.__setattr__("min_width", 20)

print(table)
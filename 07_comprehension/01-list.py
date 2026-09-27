"""MAke a list then filter from it"""

menu = [
    "Iced Tea",
    "Lemon Tea",
    "Iced Cold Cofee",
    "Masala tea",
    "Green Tea",
    "Iced peach tree",
    "Tea with sugar and milk and leaf"
]


iced_tea = [tea for tea in menu if "Iced" in tea]

print(iced_tea)

lengthy_tea = [tea for tea in menu if len(tea) > 15]

print(lengthy_tea)
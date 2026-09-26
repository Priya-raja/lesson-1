menu = ["Lemonade", "Iced Tea", "Water", "Soda", "Coffee"]

for idx,item in enumerate(menu, start=1):
    print(f"{idx} : {item}")

print(list(enumerate(menu, start=1)))    
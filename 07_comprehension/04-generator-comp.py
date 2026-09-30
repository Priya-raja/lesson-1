# Caring about memory to making it faster. Python is already slow
# Syntax (exp for item in iterable if condition) only parenthesis in memory

daily_sales = [5,10,12,7,3,8,9,15,20,18]

total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)
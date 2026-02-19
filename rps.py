import sys
import random


choices = input("enter your choice \n1. rock \n2.paper \n3.scissors \n")


if not choices.isdigit():
    print("invalid choice")
    sys.exit()
choices = int(choices)

if  choices < 1 or choices > 3:
    print("invalid choice")
    sys.exit()
computer_choice = random.randint(1, 3)
print(f"computer choice is {computer_choice}")

if choices == computer_choice:
    print("it's a tie")
elif (choices == 1 and computer_choice == 3) or (choices == 2 and computer_choice == 1) or (choices == 3 and computer_choice == 2):
    print("you win")
else:
    print("computer wins")

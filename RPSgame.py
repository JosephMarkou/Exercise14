import random

options = {"r": "rock", "p": "paper", "s": "scissors"}

user = input("Please type the first letter: rock (r), paper (p), or scissors (s): ")
computer_choice = random.choice(list(options.keys()))

print("You have chosen", options[user])
print("The computer has chosen", options[computer_choice])

if user == computer_choice:
    print("Draw")
elif user == "r" and computer_choice == "s":
    print("You Win")
elif user == "p" and computer_choice == "r":
    print("You Win")
elif user == "s" and computer_choice == "p":
    print("You Win")
else:
    print("You Lose")

# Cheating -

import random

options = {"r": "rock", "p": "paper", "s": "scissors"}

user = input("Choose rock (r), paper (p), or scissors (s): ")
computer_choice = random.choice(list(options.keys()))

print("You have chosen", options[user])
print("The computer has chosen", options[computer_choice])

win_conditions = lambda user_choice, computer_choice: (
    user_choice == "r" and computer_choice == "s" or
    user_choice == "p" and computer_choice == "r" or
    user_choice == "s" and computer_choice == "p"
)

if user == computer_choice:
    print("Draw")
elif win_conditions(user, computer_choice):
    print("You Win")
else:
    print("You Lose")

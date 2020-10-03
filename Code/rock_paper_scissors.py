import random

def main():
    options = ["rock", "paper", "scissors"]
    comp = random.choice(options)
    choice = int(input("1 for Rock, 2 for Paper, 3 for Scissors? "))
    user = options[choice-1]
    print("Computer: ", comp)
    print("User: ", user)


main()

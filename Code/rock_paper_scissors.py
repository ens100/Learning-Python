"""Rock, Paper, Scissors game - Comp vs User"""

from random import randint

user_score = 0
comp_score = 0
count_games = 1

while True: #Keep the game running TODO: give the user an easy out.

    choice = {1 : "Rock", 2: "Paper", 3 : "Scissors"}

    # User selection and randomise the comp selection:
    user = int(input("What is your weapon? (1 : Rock, 2: Paper, 3 : Scissors) ")) # TODO add in input control
    user_choice = (choice[user])
    comp_choice = (choice[randint(1,3)])

    print("---User: {} vs Comp: {}". format(user_choice, comp_choice))
    
    # Go through the cycle of win, lose or draw:
    if user_choice == "Rock" and comp_choice == "Scissors":
        print("---WIN---")
        user_score += 1
    elif user_choice == "Rock" and comp_choice == "Paper":
        print("---LOSE---")
        comp_score += 1
    elif user_choice == "Paper" and comp_choice == "Rock":
        print("---WIN---")        
        user_score += 1
    elif user_choice == "Paper" and comp_choice == "Scissors":
        print("---LOSE---")
        comp_score += 1
    elif user_choice == "Scissors" and comp_choice == "Paper":
        print("---WIN---")        
        user_score += 1
    elif user_choice == "Scissors" and comp_choice == "Rock":
        print("---LOSE---")
        comp_score += 1
    else:
        print("---DRAW---")
    
    # print out KPI of games (score, count)
    print("User: {} - Comp {}" .format(str(user_score), str(comp_score)))
    print("Games: " + str(count_games))
    
    count_games += 1

    

    

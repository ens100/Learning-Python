# V1 of Blackjack game - currently only gets user cards

import random

def blackjack():

    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11]
    card_list = []
    user_amount = 0
    

    while True:
        user_choice = input("Card? ")
        if user_choice == "y":
            card_random = random.choice(cards)
            user_amount += card_random
            card_list.append(card_random)
            
            print("Cards so far: {}" .format(card_list))
            print(user_amount)

            if user_amount == 21:
                play_again = input("Blackjack! Play Again? ")
                if play_again == "y":
                    blackjack()
                else:
                    print("Goodbye")
                break
            elif user_amount > 21:
                try_again = input("You Lose. Play Again? ")
                if try_again == "y":
                    blackjack()
                else:
                    print("Goodbye")
                break

blackjack()


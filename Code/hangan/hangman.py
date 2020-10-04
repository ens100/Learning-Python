import random

def get_word():
    # Returns random word.
    words = ['Charlie', 'Woodstock', 'Snoopy', 'Lucy', 'Linus',
             'Schroeder', 'Patty', 'Sally', 'Marcie']
    return random.choice(words).upper()

def check(word,guesses):
    '''Creates and returns string representation of word
    displaying asterisks for letters not yet guessed.'''
    status = '' #Current status of guess
    last_guess = guesses[-1]
    matches = 0 #Number of occurences of last_guess in word
    
    for letter in word:
        status += letter if letter in guesses else "*"
    
        if letter == last_guess:
            matches += 1

    if matches > 1:
        print("The word has " + str(matches) + " " + last_guess)
    elif matches == 1:
        print("The word has 1 " + last_guess)
    else:
        print("Sorry, the word has no " + last_guess + " try again")
    
    return status, "Guesses: " + str(len(guesses))

def main():
    word = get_word() #the random word
    n = len(word) #the number of letters in the random word
    guesses = [] #the list of guesses made so far
    guessed = False
    print('The word contains {} letters.'.format(n))
    
    while not guessed:
        guess = input('Guess a letter or a {}-letter word: '.format(n))
        guess = guess.upper()
        if guess in guesses:
            print("You have already guessed " + guess)
        elif len(guess) == n:
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print("sorry " + guess + " is not correct, try again.")
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(word,guesses)      
            if result == word:
                guessed = True
            else:
                print(result)
        else:
            print("Invalid guess")


    print('{} it is! It took {} tries.'.format(word, len(guesses)))
    
main()

import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y or N: " % get_close_matches(word, data.keys())[0]).lower()
        if yn == "y" :
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return "Word does not exist. Try again."
        else:
            return "Did not understand you." 
    elif word == "qq":
        return "Goodbye"
    else: 
        return "Word does not exist. Try again."

word = ""

while word != "qq":
    word = input("What Word? ")    
    output = translate(word)

    if type(output) == list:
        for number, letter in enumerate(output, start = 1):
            print(number, letter)
    else:
        print(output)



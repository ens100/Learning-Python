def main():
    word = input("What is your word? ")
    string = word.replace(" ", "")
    w = string[::-1]
    if string == w:
        print("Great, {} is a Palindrome".format(word))
    else:
        print("Sorry, {} is not a Palindrome here".format(word))
    if input("Try Again y/n? ") == "y":
        main()
    else: 
        print("goodbye")

main()

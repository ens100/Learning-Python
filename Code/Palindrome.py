def main():
    word = input("What is your word? ")
    w = word[::-1]
    if word == w:
        print("Great, {} is a Palindrome".format(word))
    else:
        print("Sorry, {} is not a Palindrome here".format(word))
    if input("Try Again y/n? ") == "y":
        main()
    else: 
        print("goodbye")

main()

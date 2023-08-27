"""
Generate a random four-digit number. The player has to keep inputting four-digit numbers until they guess the
randomly generated number. After each unsuccessful try it should say how many numbers they got correct, but not which
position they got right. At the end of the game should congratulate the user and say how many tries it took.
"""

import random


def get_random_combination():
    """
    randomly creates a 4-digit number
    :return: a 4-digit number as a string
    """
    guess = ""
    for i in range(4):
        rnd = random.randint(0, 9)
        guess = guess + str(rnd)
    #next i
    return guess
# end def


def get_guess():
    """
    get the user to enter a 4-digit number.
    :return: the 4-digit number input
    """
    guess = ""
    valid = False
    while not valid:
        guess = input("Enter a four digit number: ")
        if len(guess) == 4 and guess.isnumeric():
            valid = True
        else:
            print("You must enter a 4 digit number")
        #end if
    #end while
    return guess
# end def


def check_guess(guess, secret, tries):
    """
    check the guess against the secret and
    display the result
    :return: True or False
    """
    total_correct = 0
    if guess == secret:
        print("You got it correct in " + str(tries) + " tries. Well done")
        return True
    #end if
    for i in range(4):
        if guess[i] == secret[i]:
            total_correct = total_correct + 1
        #end if
    #next i
    print("You got " + str(total_correct) + " correct")
    return False
#end def


def main():
    secret = get_random_combination()
    print(secret)
    total_tries = 1
    correct = False
    while not correct:
        guess = get_guess()
        correct = check_guess(guess, secret, total_tries)
        total_tries = total_tries + 1
    #end while
#end def


if __name__ == "__main__":
    main()
#end if

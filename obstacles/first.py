from replit import clear
import time
import random
from replit import audio
from colorama import Fore, Back, Style
from enter_to_continue import *



def first_obstacle():
    '''User will need to guess a number between 0 and 5. Correct number will be randomly generated'''

    print("Welcome to your life as a birb!\n\nYou have a lot on the agenda toaday.\nLet's get started with your birb duties!")
    print()
    enter_to_continue()
    print("Before you leave your nest, you need to pay the seed toll.")
    

    #variable to store number of wrong guesses
    wrong_guesses = 0

    #randomly generate correct number of seeds and store in variable
    correct_seeds = random.randint(0, 3)

    while True:
        #ask user for number between 0 and 3
        seed_guess = input("How many seeds will you be providing?\n\nPlease give an amount between 0 and 3:\n> ")
        clear()

        #condition if user inputs anything other than a number
        if seed_guess.isalpha():
            print("That is an invalid answer!")
            print()
            continue

        #convert user input from string to integer
        seed_guess = int(seed_guess)

        #condition for when correct number above 0 is guessed
        if seed_guess == correct_seeds and seed_guess > 0:
            print("Correct! Well done.\nNow hand over the seeds and you'll be on your way.")
            print()

            #transition to continue to next screen
            enter_to_continue()
            break

        #condition for when incorrect number is guessed  
        elif seed_guess >= 0 and seed_guess <= 3 and seed_guess != correct_seeds:
            print("That is an unacceptable number of seeds! Please try again.")

            #add count to number of wrong guesses and print
            wrong_guesses += 1
            print(Fore.RED + f"Wrong guesses: {wrong_guesses}")
            print(Fore.WHITE)

        #condition for when correct number (0) is guessed
        elif seed_guess == correct_seeds and seed_guess == 0:
            print("...That is correct. This was just a trick question. Carry on.")
            print()

            #transition to continue to next screen
            enter_to_continue()
            break

        #condition for when anything outside of integers 0-3 is inputted
        else:
            print("That is an invalid answer.")
            print()

first_obstacle()
clear()
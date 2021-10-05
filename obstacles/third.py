from replit import clear
import time
import random
from replit import audio
from colorama import Fore, Back, Style
from enter_to_continue import *
from bird_generator import *


def another_hangman_game():
  '''ask user if they want to play hangman again'''
  
  while True:
    answer = input("Would you like to play hangman again? ")
    answer = answer.lower()
  
    if answer =="no" or answer == "yes":
      return answer
    else:
      print("That is not a valid answer")
      print()
    


def third_obstacle():
    '''User will play a game of Hangman by guessing letters'''

    #print statements introducitng third obstacle
    print(f"Good job escaping from that cat!\n\nI knew you could do it,{name}.")
    print()
    print("Now it's time to fly over to your friend's tree to play a game of hangman with some of the local birbs.\n\naka: important birb duties.")
    print()

    #transition to continue to next screen
    enter_to_continue()

    while True:
        #select word for handman at random
        list_of_words = {"EGGS": "____", "BIRBS R DA BEST": "_____ _ __ ____", "PARAKEET": "________", "TALONS": "______", "FEATHERS": "________"}

        selected_word, spaces = random.choice(list(list_of_words.items()))
        

        incorrect_letters = ""
        correct_letters = ""
        turns = 0


        while turns < 5:
            print(spaces)
            print()
            guessed_letter = input("Please guess a letter: ")
            guessed_letter = guessed_letter.upper()
            clear()
            
            #if correct letter is guessed
            if guessed_letter in selected_word:
                print(Fore.CYAN + "That letter is correct!")
                print(Fore.WHITE)
                correct_letters += guessed_letter
                print(f"Incorrect letters used: {incorrect_letters}")
                print()

                #print out correct letters and remaining blanks
                for i in range(len(selected_word)): 
                    if selected_word[i] in correct_letters:
                        spaces = spaces[:i] + selected_word[i] + spaces[i+1:]

            
            #if incorrect letter is guessed
            else:
                incorrect_letters += guessed_letter + " "
                turns += 1
                #if 5 incorrect letters have been guessed
                if turns == 5:
                    print(Fore.RED + "Oh no, you lost!")
                    print(Fore.WHITE)

                    #transition to continue to next screen
                    enter_to_continue()

                    incorrect_letters = []
                    correct_letters = ""
                    continue
                    
                print(Fore.RED + "That letter is incorrect!")
                print(Fore.WHITE)
                print(f"Incorrect letters used: {incorrect_letters}")
                print()
            
            if spaces == selected_word:
                print(spaces)
                print()
                print(Fore.MAGENTA + "You won!")
                print(Fore.WHITE)
                break
        
        #determine if user wants to play another round of hangman
        answer = another_hangman_game()
        if answer == "no":
            clear()
            break
        elif answer == "yes":
            continue

    #print statements to end the third obstacle      
    print("Good game!\nOr should I say.... EGGcelent game.")
    print()

    #transition to continue to next screen
    enter_to_continue()

third_obstacle()
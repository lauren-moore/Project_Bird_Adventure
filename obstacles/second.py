from replit import clear
import time
import random
from replit import audio
from colorama import Fore, Back, Style
from enter_to_continue import *
from bird_generator import *


def second_obstacle_intro():
    '''print statements that introduce the second obstacle'''
    #print statements to introduce the second obstacle
    print("Now that you've left the nest, it's time to fly off!")
    time.sleep(2)
    print()
    print(Fore.CYAN + "BUT WAIT!!!!")
    time.sleep(2)
    print(Fore.WHITE)
    print("There is a cat sleeping on the same tree branch as your nest...\nYou could just fly away, but you are feeling adventurous and would rather walk around the cat.\n\nIt's a risky move, but you live life on the edge.....literally.\nBecause, ya know, your nest sits at the edge of this branch.")
    print()

    #transition to continue to next screen
    enter_to_continue()


def second_obstacle_stats(bird_health, successful_steps):
    '''prints current status of bird health and remaining steps to escape'''
 
    print(Fore.BLUE + f"Birb Health" + Fore.RED + " ❤ " + Fore.BLUE +  ": " + Fore.WHITE + f"{bird_health}")
    print(Fore.MAGENTA + f"Remaining steps to escape 🐱 : " + Fore.WHITE + f"{successful_steps}")
    print(Fore.WHITE)
    print()


def second_obstacle():
    '''Choose your own adventure game that will require user to input one of the answers provided'''

    second_obstacle_intro()    

    #variables to store the player's health and remaining moves required to complete the obstacle
    successful_steps = 3
    bird_health = 3

    while successful_steps > 0:

        #ask user which path they will choose
        second_obstacle_stats(bird_health, successful_steps)
        user_input_path = input("In order to sneak around the cat, you will need to choose the correct path.\nWhich path will you choose?\n\nA. Left \nB. Right \n\n> ")

        #randomly generate number to determine correct answer
        random_num_generator = random.randint(1,2)
        user_input_path = user_input_path.title()

        #assigns user input to integer to determine correct answer
        if user_input_path == "A":
            correct_guess = 1
        elif user_input_path == "B":
            correct_guess = 2

        #condition if user inputs anything other than "A" or "B"
        else:
            print()
            print("That is an invalid answer! Please select A or B.")
            print()

            #transition to continue to next screen
            enter_to_continue()
            continue

        clear()
        second_obstacle_stats(bird_health, successful_steps)

        #show that the cat is sleeping
        print("Zzzz...")
        time.sleep(2)
        clear()

        #condition if correct guess is inputted
        if random_num_generator == correct_guess:
            second_obstacle_stats(bird_health, successful_steps - 1)
            print("The cat is still fast asleep! You take a step forward.")
            successful_steps -= 1
            print()

            #transition to continue to next screen
            enter_to_continue()

        #condition if incorrect guess is inputted
        else:
            second_obstacle_stats(bird_health, successful_steps)
            user_input_choice = input("Oh no! You woke up the cat! Time to think fast on your feet.\nWhat will you do next?\n\nA. Hide behind a leaf\nB. Try to befriend the cat\nC. Sing a lullaby\n\n> ")
            user_input_choice = user_input_choice.upper()
            clear()
    
            #condition if incorrect answer is inputted
            if user_input_choice == "A":
                second_obstacle_stats(bird_health - 1, successful_steps)
                print("...Silly birb. The cat can still see you standing behind that leaf.\nFor underestimating her, she takes a swipe at you and lowers your health by 1.\nThe cat falls back asleep.")
                bird_health -= 1

                #condition if bird runs out of health
                if bird_health == 0:
                    print()
                    print("You fainted! Please try again.")
                    bird_health = 3
                    successful_steps = 3
                    clear()
                    continue
                print()

                #transition to continue to next screen
                enter_to_continue()

            #condition if neutral answer is inputted
            elif user_input_choice == "B":
                second_obstacle_stats(bird_health, successful_steps)
                print("The cat thinks you're a great conversationalist. Well done!\nAfter a fun chat, the cat falls back asleep.\nYou will still need to sneak around her because she HATES being woken up from her nap.")
                print()

                #transition to continue to next screen
                enter_to_continue()
            
            #condition if correct answer is inputted
            elif user_input_choice == "C":
                second_obstacle_stats(bird_health, successful_steps - 1)
                print("You sing a lullaby and...\n\nIT'S BEAUTIFUL\n\nThe cat falls back asleep, and you take a step forward toward freedom.")
                successful_steps -= 1
                print()

                #transition to continue to next screen
                enter_to_continue()
            
            #condition if invalid answer is inputted
            else:
                second_obstacle_stats(bird_health, successful_steps)
                print("That is an invalid answer! Please try again.")
                print()

                #transition to continue to next screen
                enter_to_continue()
                continue
    
    #print statements closing the second obstacle           
    print(f"You escaped!\n\nShe may have ruffled your feathers, but that cat was no match for {name}.")
    print()

    #transition to continue to next screen
    enter_to_continue()

second_obstacle()
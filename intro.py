from replit import clear
import time
import random
from replit import audio
from colorama import Fore, Back, Style
from enter_to_continue import *


def intro():
    '''Introduce user to the game and ask user if they are ready to start playing'''

    print(""" ▄▄▄▄▄▄▄ ▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄ ▄▄▄▄▄▄  ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄▄ 
█  ▄    █   █   ▄  █ █  ▄    █  █       █      ██  █ █  █       █  █  █ █       █  █ █  █   ▄  █ █       █
█ █▄█   █   █  █ █ █ █ █▄█   █  █   ▄   █  ▄    █  █▄█  █    ▄▄▄█   █▄█ █▄     ▄█  █ █  █  █ █ █ █    ▄▄▄█
█       █   █   █▄▄█▄█       █  █  █▄█  █ █ █   █       █   █▄▄▄█       █ █   █ █  █▄█  █   █▄▄█▄█   █▄▄▄ 
█  ▄   ██   █    ▄▄  █  ▄   █   █       █ █▄█   █       █    ▄▄▄█  ▄    █ █   █ █       █    ▄▄  █    ▄▄▄█
█ █▄█   █   █   █  █ █ █▄█   █  █   ▄   █       ██     ██   █▄▄▄█ █ █   █ █   █ █       █   █  █ █   █▄▄▄ 
█▄▄▄▄▄▄▄█▄▄▄█▄▄▄█  █▄█▄▄▄▄▄▄▄█  █▄▄█ █▄▄█▄▄▄▄▄▄█  █▄▄▄█ █▄▄▄▄▄▄▄█▄█  █▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄█  █▄█▄▄▄▄▄▄▄█
""")

    #text for title screen
    print(38 * " " + Fore.CYAN + Style.BRIGHT + "Welcome to Birb Adventure!")
    print()
    print(35 * " " + "🦆 🦩 🐓 🐦 🐧 🦢 🦅 🐥 🦚 🦉 🦜")
    print()
    print(Fore.YELLOW + 105 *"*")
    print(Fore.WHITE)
    print()

    while True:
        start_game = input("Are you ready to play? (Y/N) ")
        print()

        # if user does not want to play
        if start_game.upper() == "N":
            print("See ya later!")
            break

        # if user does want to play
        if start_game.upper() == "Y":
            print("Hooray! Let's get started.")
            print()

            #transition to continue to next screen
            enter_to_continue()

            break
        else:
            print("Oops! That is an invalid answer. Please select Y or N.")

intro()
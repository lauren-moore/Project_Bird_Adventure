from replit import clear
import time
import random
from replit import audio
from colorama import Fore, Back, Style
from enter_to_continue import *


def loading_screen():
    '''loading screen to simulate character name generating'''
    generating_char = "Generating birb..."
    bird_emojis = "🦆 🦩 🐓 🐦 🐧 🦢 🦅 🐥 🦚 🦉 🦜"

    #loading screen for text
    for i in range(len(generating_char)):
        print(generating_char[i], end ='', flush=True); time.sleep(0.1)
    time.sleep(1)
    print()

    #loading screen for bird emojis
    for i in range(len(bird_emojis)):
        print(bird_emojis[i], end ='', flush=True); time.sleep(0.2)
    time.sleep(1)
    clear()

def bird_generator():
    '''Ask user for name and adjective for their character. Generate their bird type'''

    print("""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██ ▄▄▀██▄██ ▄▄▀█ ▄▄▀████ ▄▄▀█ ▄▄▀█ ▄▄█ ▄▄▀█▄ ▄█▀▄▄▀█ ▄▄▀██
██ ▄▄▀██ ▄█ ▀▀▄█ ▄▄▀████ ████ ▀▀▄█ ▄▄█ ▀▀ ██ ██ ██ █ ▀▀▄██
██ ▀▀ █▄▄▄█▄█▄▄█▄▄▄▄████ ▀▀▄█▄█▄▄█▄▄▄█▄██▄██▄███▄▄██▄█▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀""")
    print()

    #list of different bird types
    bird_types = ["Pigeon", "Seagull", "Robin", "Sparrow", "Turkey", "Chicken", "Flamingo", "Peacock", "Pelican"]

    #print the list of bird types
    for bird in bird_types:
        print(5*" " + "-" + bird)
    print()
    print("Let's find out what kind of birb you are!")
    print()

    #Ask user for name of their character
    bird_name = input("Name of your birb: ")

    #Ask user for an adjective 
    bird_adj = input("Please provide an adjective: ")

    #Convert user inputs to title case
    bird_name = bird_name.title()
    bird_adj = bird_adj.title()


    #select bird type from above list at random
    selected_bird_type = random.choice(bird_types)
    clear()

    loading_screen()
   
    #print statement introducing character name, adjective, bird type
    global name
    name = f"✨{bird_name} the {bird_adj} {selected_bird_type}✨"
    print(f"And now introducing... \n\n       {name}!")
    print()
    print()

    #transition to continue to next screen
    enter_to_continue()

bird_generator()
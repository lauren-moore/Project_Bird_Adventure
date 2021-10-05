from replit import clear
import time
import random
from replit import audio
from colorama import Fore, Back, Style
from bird_generator import *


def end_of_game():
    '''print statements to end the game'''

    #closing statment
    print(f"Well I think those were enough birb duties for one day.\nAs you can see, it's a lot of work being a birb!\n\nThanks for joining, {name}!")
    print()
    time.sleep(2)
    print("See you next time on...")
    time.sleep(1)
    print(""" ▄▄▄▄▄▄▄ ▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄ ▄▄▄▄▄▄  ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄▄ 
█  ▄    █   █   ▄  █ █  ▄    █  █       █      ██  █ █  █       █  █  █ █       █  █ █  █   ▄  █ █       █
█ █▄█   █   █  █ █ █ █ █▄█   █  █   ▄   █  ▄    █  █▄█  █    ▄▄▄█   █▄█ █▄     ▄█  █ █  █  █ █ █ █    ▄▄▄█
█       █   █   █▄▄█▄█       █  █  █▄█  █ █ █   █       █   █▄▄▄█       █ █   █ █  █▄█  █   █▄▄█▄█   █▄▄▄ 
█  ▄   ██   █    ▄▄  █  ▄   █   █       █ █▄█   █       █    ▄▄▄█  ▄    █ █   █ █       █    ▄▄  █    ▄▄▄█
█ █▄█   █   █   █  █ █ █▄█   █  █   ▄   █       ██     ██   █▄▄▄█ █ █   █ █   █ █       █   █  █ █   █▄▄▄ 
█▄▄▄▄▄▄▄█▄▄▄█▄▄▄█  █▄█▄▄▄▄▄▄▄█  █▄▄█ █▄▄█▄▄▄▄▄▄█  █▄▄▄█ █▄▄▄▄▄▄▄█▄█  █▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄█  █▄█▄▄▄▄▄▄▄█
""")

    print()

    time.sleep(1)

    #fun image provided via hyperlink 
    print("Click this link! ⬇")
    print("https://i.redd.it/r4beqjhbegp71.jpg")
    print()

    #credits/references provided below
    print("Credits")
    print("Copyright Music: https://www.fesliyanstudios.com/royalty-free-music/downloads-c/8-bit-music/6")
    print("Title screen text: https://texteditor.com/multiline-text-art/")
    input(Fore.GREEN + "Press ENTER to quit ") 
    print(Fore.WHITE)
    clear()         

end_of_game()
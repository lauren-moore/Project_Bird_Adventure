'''Birb Adventure'''

from replit import clear
import time
import random
from replit import audio
from colorama import Fore, Back, Style
from enter_to_continue import *
from intro import *
from bird_generator import *
from obstacles.first import *
from obstacles.second import *
from obstacles.third import *
from end_of_game import *

#play music
while True:
    source = audio.play_file('8-bit-song.mp3')
    time.sleep(10)
    break

#title screen and introduction to game
intro()

#bird generator - create your character
character_title()

#seed toll game
first_obstacle()

#birb vs cat - choose your own adventure game
second_obstacle()

#hangman
third_obstacle()
     
#credits and ending title screen
end_of_game()
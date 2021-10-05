from replit import clear
from colorama import Fore, Back, Style


def enter_to_continue():
    '''prompts user to press "Enter" key to clear screen'''
    press_enter = input(Fore.GREEN + "Press ENTER to continue ")
    print(Fore.WHITE)
    clear()
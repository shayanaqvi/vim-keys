#!/usr/bin/env python3

from os import *
import time
import os

def print_cheatsheet():
    if os.path.isfile('keybindings.txt') == True:
        print("")
        print("-----------------------")
        print(" Basic Vim Keybindings ")
        print("-----------------------")
        print("")

        time.sleep(1)

        system('cat keybindings.txt')
        print("")
    else:
        print("Is the file, 'keybindings.txt', in the same directory as the executable?")

print_cheatsheet()

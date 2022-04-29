# Import Libraries
import os
import time

from art import *
from termcolor import colored
from itertools import permutations


# Class Definition
class AppTools:
    def ClearTerminal(self):
        os.system('cls' if os.name=='nt' else 'clear')

# Class String
AppTools = AppTools()


class Application:
    def WelcomeMsg(self):
        AppTools.ClearTerminal()
        tprint('Cenera', font='bulbhead')
        time.sleep(1)
        print()

    def EnterInfo(self):
        global AllLetters
        AllLetters = input(colored('String: ', 'green', attrs=['bold']))

    def GenerateAll(self):
        # Possible Strings
        LettersLength = len(AllLetters)
        LettersLength = int(LettersLength)

        # Check Length
        if LettersLength < 2:
            print()
            print(colored('Invalid Length #2', 'red', attrs=['bold']))
            time.sleep(1.5)
            AppTools.ClearTerminal()
            MainApp.EnterInfo()

        # Generate List
        global Permutations
        Permutations = [''.join(p) for p in permutations(AllLetters)]
        PossiblePermutations = len(Permutations)

        # Print Generation Process
        print()
        print(colored('Generating '+str(PossiblePermutations)+' Strings ...', 'green', attrs=['bold']))
        time.sleep(1.5)
        AppTools.ClearTerminal()
        print(*Permutations, sep = '\n')

    def SavePerms(self):
        # Create Folder
        if not os.path.exists('perms'):
            os.makedirs('perms')

        # Create & Write File
        with open('perms/'+AllLetters+'.lst', 'w') as File:
            File.write('\n'.join(map(str, Permutations)))

        # Print
        print()
        print(colored('Wordlist Generated!', 'green', attrs=['bold']))
        print(colored('/perms/'+AllLetters+'.lst', 'grey'))
        print()


# Class String
MainApp = Application()


# Run
MainApp.WelcomeMsg()
MainApp.EnterInfo()
MainApp.GenerateAll()
MainApp.SavePerms()
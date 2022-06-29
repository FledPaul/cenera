# Import Libraries
import os
import time
import shlex

from art import *
from termcolor import colored
from itertools import permutations

# Intern Functions
class RunIn:
    @staticmethod
    def ClearTerminal():
        os.system(shlex.quote('cls' if os.name == 'nt' else 'clear'))

# Define Class
InternFunctions = RunIn()

# Application
class Application:
    @staticmethod
    def WelcomeMsg():
        InternFunctions.ClearTerminal()
        tprint('Cenera', font='bulbhead')
        time.sleep(1)
        print()

    @staticmethod
    def UserInfo():
        global SelectedCharacters
        SelectedCharacters = input(colored('Your Word: ', 'green', attrs=['bold']))

    @staticmethod
    def RunProcess():
        LettersLength = len(SelectedCharacters)
        LettersLength = int(LettersLength)

        if LettersLength < 2:
            print()
            print(colored('Invalid Length #1'))
            time.sleep(1.5)
            InternFunctions.ClearTerminal()
            App.UserInfo()

        global PermList
        PermList = [''.join(p) for p in permutations(SelectedCharacters)]
        PossiblePermList = len(PermList)
        print()

        print(colored('Generating '+str(PossiblePermList)+' Strings ...', 'green', attrs=['bold']))
        time.sleep(1.5)
        InternFunctions.ClearTerminal()
        print(*PermList, sep = '\n')

    @staticmethod
    def SavePerms():
        if not os.path.exists('perms'):
            os.makedirs('perms')

        with open('perms/'+SelectedCharacters+'.lst', 'w') as PermFile:
            PermFile.write('\n'.join(map(str, PermList)))

        print()
        print(colored('Wordlist Generated!', 'green', attrs=['bold']))
        print(colored('/perms/'+SelectedCharacters+'.lst', 'grey'))
        print()

# Define Class
App = Application()

# Run Application
App.WelcomeMsg()
App.UserInfo()
App.RunProcess()
App.SavePerms()
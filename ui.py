# Import Libraries
import sys
import time
import os

from itertools import permutations
from datetime import date
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton

class AppWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # GUI Style
        self.setWindowTitle('Cenera - Permutations Made Simple')
        self.setFixedSize(650, 225)
        self.setStyleSheet('background-color: #FFFFFF;')

        # Characters Input
        self.Characters = QLineEdit(self)
        self.Characters.move(35, 35)
        self.Characters.resize(580, 60)
        self.Characters.setPlaceholderText('Characters')
        self.Characters.setStyleSheet('border: none; border-radius: 20px; background: 20px; background-color: #EEEEEE; color: #606060; padding-left: 10px; font-weight: 500; font-size: 15px;')

        # Generate Function
        def Generate():
          # Get Current Date
          Date = date.today()
          Date = Date.strftime('%b-%d-%Y')

          # Create Log Folder
          if not os.path.isdir('log'):
            os.mkdir('log')
            print('Success : Log Directory Created')

          # Delete (Existing) Log File
          if os.path.isfile('log/' + Date + '.log'):
            os.remove('log/' + Date + '.log')
            print('Success : Old Log File Deleted')

          # Create Log File
          LogFile = open('log/' + Date + '.log', 'a')
          print('Success : New Log File Created')
          LogFile.write('Success : New Log File Created\n')

          #####################################################

          # Get Chars & Length
          Chars = self.Characters.text()
          CharsLength = len(Chars)
          CharsLength = int(CharsLength)

          if CharsLength < 2:
            print('Error : Invalid Length')
            LogFile.write('Error : Invalid Length\n')
            time.sleep(2)
            sys.exit()

          # Generate Perms
          PermList = [''.join(p) for p in permutations(Chars)]

          # Save Perms
          if not os.path.exists('perms'):
            os.makedirs('perms')
            print('Success : Permutation Directory Created')
            LogFile.write('Success : Permutation Directory Created\n')
          elif os.path.exists('perms'):
            print('Success : Directory Exists')
            LogFile.write('Success : Directory Exists\n')
          else:
            print('Error : Something Went Wrong')
            LogFile.write('Error : Something Went Wrong\n')
            time.sleep(2)
            sys.exit()

          with open('perms/' + Chars + '.lst', 'w') as PermFile:
            PermFile.write('\n'.join(map(str, PermList)))
            print('Success : Permutations Written')
            LogFile.write('Success : Permutations Written')

          # Change 'Generate' To 'Saved'
          self.GenerateBtn.setText('Generated')
          print('Success : Process Finished')
          LogFile.write('Success : Process Finished\n')

        # Generate Button
        self.GenerateBtn = QPushButton('Generate', self)
        self.GenerateBtn.move(35, 130)
        self.GenerateBtn.resize(580, 60)
        self.GenerateBtn.setStyleSheet('border: none; border-radius: 20px; background-color: #006EE6; color: #FFFFFF; font-weight: 500; font-size: 15px;')
        self.GenerateBtn.clicked.connect(Generate)

# UI Intialization
if __name__ == '__main__':
    App = QtWidgets.QApplication(sys.argv)
    AppWindow = AppWindow()
    AppWindow.show()
    sys.exit(App.exec())

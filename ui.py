# Import Libraries
from itertools import permutations
import sys
import json
import time
import os

from datetime import date
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton


# Automatic Library Installation
class SetUp:
  def AutoUpdate(self):
    AutoUpdate = open('json/alis.json', 'r+')
    AutoUpdateData = json.load(AutoUpdate)   
    # Check Update
    if AutoUpdateData['updated'] is False:
      time.sleep(1)
      print()
      RequiredLibs = AutoUpdateData['libs'].split(' ')
      CurrentLibCount = -1
      # Update Libraries
      for i in range(len(RequiredLibs)):
        CurrentLibCount = CurrentLibCount + 1
        os.system('pip install ' + RequiredLibs[CurrentLibCount])
        # Update 'Updated' To 'True'
        UpdateData = {"updated": True, "libs": AutoUpdateData['libs']}
        AutoUpdate.seek(0)
        AutoUpdate.truncate()
        json.dump(UpdateData, AutoUpdate, indent=2)
        print('Dependencies Installed!')

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

          # Delete (Existing) Log File
          try:
              os.remove(Date + '.log')
          except FileNotFoundError:
              pass

          # Create Log File
          LogFile = open(Date + '.log', 'a')

          #####################################################

          # Get Chars & Length
          Chars = self.Characters.text()
          CharsLength = len(Chars)
          CharsLength = int(CharsLength)

          if CharsLength < 2:
            print('Error : Invalid Length')
            LogFile.write('Error : Invalid Length')
            time.sleep(2)
            sys.exit()

          # Generate Perms
          PermList = [''.join(p) for p in permutations(Chars)]

          # Save Perms
          if not os.path.exists('perms'):
            os.makedirs('perms')
            print('Success : Directory Created')
            LogFile.write('Success : Directory Created')
          elif os.path.exists('perms'):
            print('Success : Directory Exists')
            LogFile.write('Success : Directory Exists')
          else:
            print('Error : Something Went Wrong')
            LogFile.write('Error : Something Went Wrong')
            time.sleep(2)
            sys.exit()

          with open('perms/'+Chars+'.lst', 'w') as PermFile:
            PermFile.write('\n'.join(map(str, PermList)))

          # Change 'Generate' To 'Saved'
          self.GenerateBtn.setText('Generated')

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
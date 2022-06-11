# Import Libraries
import sys
import json
from xml.dom.expatbuilder import theDOMImplementation

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


# Default Variable
theme = 'light'


# Class Definition
class GetConfig:
    def LoadJson(self):
        with open('config.json') as f:
            global data
            data = json.load(f)
            print(data)

    def GetTheme(self):
        if data['theme'] == 'light':
            theme = 'light'
        elif data['theme'] == 'dark':
            theme = 'dark'
        else:
            try:
                errlog = open('error.log', 'w')
                errlog.write('Error : Invalid Theme - Select between "dark" and "light"')
            except:
                print('Error : Something Went Wrong')
            exit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Cenera - Permutations Made Simple')
        self.setFixedSize(900,260)


# Theme Intialization
getcfg = GetConfig()
getcfg.LoadJson()
getcfg.GetTheme()


# UI Intialization
app = QApplication([])
window = QWidget
window.show()
app.exec()
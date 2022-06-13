# Import Libraries
import json
import time
import os

class SetUp:
  def AutoUpdate(self):
    AutoUpdate = open('autoupdate.json', 'r+')
    AutoUpdateData = json.load(AutoUpdate)   
    # Check Update
    if AutoUpdateData['updated'] == False:
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
    # Run Main
    os.system('main.py')
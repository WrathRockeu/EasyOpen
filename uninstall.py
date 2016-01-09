#This will delete the autorun programs
import os
import os.path
import getpass

#Get the current folder path
cwd = os.getcwd()

#Get the current username, needed to delete vbs
username = getpass.getuser()

#Delete the .vbs file in the startup folder
startpath = 'C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\' %(username)
os.system('del "%sEasyOpen.vbs"' %(startpath))

#Delete the hidden .EOSys folder
os.system('RMDIR /S /Q "%s\\.EOSys"' %(cwd))

#This file will create a VBScript and a Command Line file to run the program
import os
import os.path
import getpass

#Get the path of the current folder. This will be used in the created scripts.
path = os.getcwd()

#Get the current username, this is needed
username = getpass.getuser()

#Get the path of the startup folder
startpath = 'C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\' %(username)
#UPDATING FROM v0.1 or 0.2: DELETE OLD runEO.cmd FILE     
if os.system('dir "%srunEO*"' %(startpath)) == 0 :
    os.system('del "%srunEO*"' %(startpath))

#Create the auto-run vbs script
vbs = open("%s" %(startpath) + 'EasyOpen.vbs', 'w')
script = """Set oShell = CreateObject("WScript.Shell")
Dim strArgs
strArgs = "cmd /c %s\\.EOSys\\runEO.cmd"
oShell.Run strArgs, 0, false""" %(path)
vbs.write(script)
vbs.close()

#Now create the .EOSys folder and make it hidden
os.system('mkdir %s\.EOSys' %(path))
os.system('attrib +h %s\.EOSys' %(path))

#Make the README that explains not to mess around in this folder
readme = open('.EOSys\\README.txt', 'w')
string = """IMPORTANT; Do not touch anything in this folder, as everything in here
is necessary to the running of the program, just trust me"""
readme.write(string)
readme.close()

#Lastly, create the CMD file to run the program
cmd = open('.EOSys\\runEO.cmd', 'w')
command = """@ECHO OFF
cd %s
call EasyOpen.py""" %(path)
cmd.write(command)
cmd.close()

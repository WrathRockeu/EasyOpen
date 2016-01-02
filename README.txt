EasyOpen Version 0.1 (Beta)

==What it does==
EasyOpen allows you to create groups of shortcuts to open at once when you start up your computer.
You can create as many groups as you want and then select the groups you wish to open so you only open what you need.

==Setup==
1)Please download Python3.4 and install it onto your computer from this link:
  https://www.python.org/downloads/release/python-343/

2)Take note of the path of the folder in which EasyOpen.py is located. To do this, right click on EasyOpen.py,
  click on Properties and take note of the "Location" information on the window.

3)Right click on runEO.cmd and click Edit. Follow the instructions at the top to set it up correctly.

4)This part depends on your Operating System. Right click on runEO.cmd and click Copy, then follow the
  follow the steps below for your OS.

  ==Windows 8/10==
  1)Press the Start button, type Run and press Enter
  2)In the Run window, type shell:startup to open the Startup folder
  3)Right click and select paste to paste a copy of runEO.cmd into the folder

  ==Windows 7==
  1)Click Start, then Programs or All Programs. Find the Startup folder, 
    right click it and select Open
  2)Right click and select paste to paste a copy of runEO.cmd into the folder

5)Done! The script should run automatically on startup now.

*IMPORTANT* If you move the EasyOpen.py file to a different folder, make sure you update the runEO file in the
Startup folder!

==How to Use==
Groups are made in this program by making subfolders in the folder containing EasyOpen.py. To make a group, simply
right-click in this folder, click New, and create a New Folder. The name of the folder will be the name of the group.
To add programs to this group, create shortcuts to the program in the group's folder. The program will run all shortcuts
in each selected group.

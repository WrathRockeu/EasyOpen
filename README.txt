EasyOpen Version 0.3 (Beta)

==What it does==
EasyOpen allows you to create groups of shortcuts to open at once when you start up your computer. You can create as many groups as you want and then select the groups you wish to open so you only open what you need.

==Setup==
In v0.3, everything becomes a lot more automated. All you have to do is run setup.py and you're good to go!

A couple of things to note:
1) setup.py will delete the old auto-run script for you, if you are updating from an older version. However, to ensure a proper update, please delete any files in
your EasyOpen directory not in the following list: EasyOpen.py, README.txt and setup.py. You do not have to recreate your groups.

2) If you move your EasyOpen directory after running setup.py, please run it again to ensure the automation stays working fully

3) Please also note that for now, you still require an installation of Python3.4, obtainable here: https://www.python.org/downloads/release/python-343/
==How to Use==
Groups are made in this program by making subfolders in the folder containing EasyOpen.py. To make a group, simply right-click in this folder, click New, and create a New Folder. The name of the folder will be the name of the group. To add programs to this group, create shortcuts to the program in the group's folder. The program will run all shortcuts in each selected group.

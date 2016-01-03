import os
import os.path
from tkinter import *
import re

class EasyOpen(Tk) :
    #The main class of the window that will be used
    
    ##Class Constants
    #Title of the window
    _TITLE = 'EasyOpen v0.2'
    #Row to start placing widgets
    _ROW = 1

    def __init__(self, master, title=_TITLE) :
        #Constructor for the EasyOpen window
        
        #Run the super constructor
        Tk.__init__(self, master)
        
        #Set the title
        self.title(title)
        
        #Override default 'X' button command
        self.protocol('WM_DELETE_WINDOW', self._cancel)
        
        #Create a help label at the top
        label = Label(self, text="Select the groups to open and click Open", anchor=CENTER)
        label.grid(row=0, column=0, columnspan=2)
        
        #Initialise the checkboxes
        self._initialiseCheckboxes()
        
        #Initialise the confirm buttons
        self._initialiseButtons()
        
        #Remove resizability
        self.resizable(False, False)
        
        #Center the window
        _center(self)

    def _initialiseCheckboxes(self) :
        #Create the checkboxes using names of group folders

        #Get the global list of group folders
        global dirs
        #List for storing the checkboxes to find the checked ones on accept
        self._checkboxes = []
        
        #Create local variables
        column = 0
        sticky = 'W'
        
        #Loop through dirs, regex out the .// and use it as the checkbox label
        for subdir in dirs :
            row = EasyOpen._ROW
            subdir = re.compile(r'.\\').sub('', subdir)
            variable = IntVar()
            checkbox = Checkbutton(master=self, text=subdir, variable=variable)
            checkbox.variable = variable
            checkbox.label = subdir
            self._checkboxes.append(checkbox)
            checkbox.grid(row=row, column=column, sticky=sticky)
            column = column + 1
            if column > 1 :
                #New row, reset columns
                column = 0
                EasyOpen._ROW += 1


    def _initialiseButtons(self) :
        #Construct and add the buttons for confirm and cancel
        
        #Create local variables
        row=EasyOpen._ROW + 1
        column=0
        sticky='WE'
        
        #Create and add confirmation button
        confirm = Button(master=self, text="Open", command=self._confirm)
        confirm.grid(row=row, column=column, sticky=sticky)
        column += 1
        
        #Create and add cancel button
        cancel = Button(master=self, text="Cancel", command=self._cancel)
        cancel.grid(row=row, column=column, sticky=sticky)
        
    def _cancel(self) :
        #Display a new window prompting confirmation of cancellation

        #Create local variables for label text and confirmation function
        label = "Do you wish to cancel?"
        confirm = self.destroy

        #Create a prompt window
        prompt = self._createPrompt('Cancel', label, confirm)
        
    def _confirm(self) :
        #Display a new window showing the selected groups and prompt confirmation
        
        #Get the global list of group directories
        global dirs
        
        #Get all the selected checkboxes on the main window
        selected = [checkbox for checkbox in self._checkboxes if checkbox.variable.get() == 1]
        
        #Create a string to display all selected directories in an easy to read format
        dir_string = ''
        for checkbox in selected :
            if checkbox == selected[-1] :
                dir_string += checkbox.label
            else :
                dir_string += checkbox.label + '\n'

        #Save this list for the open function
        self._selected = selected
        
        #Create local variables for label text and confirmation function
        label = "You have selected the following groups:\n%s\nDo you wish to open these?" %(dir_string)
        confirm = self._open

        #Create the prompt
        self._createPrompt('Confirm Groups', label, confirm)
        
        
    def _createPrompt(self, title, label, confirm) :
        #Creates a window with a label and two buttons, with the title 'title', 'label' as the label's text and 'confirm' as the command of the yes button

        #Create a TopLevel window
        prompt = Toplevel()

        #Take all focus
        prompt.grab_set()

        #Apply the passed title
        prompt.title(title)

        #Create the widgets
        Label(master=prompt, text=label, anchor=CENTER).grid(row=0, column=0, columnspan=2, sticky="WE")
        Button(master=prompt, text="Yes", command=confirm).grid(row=1, column=0, sticky="WE")
        Button(master=prompt, text="No", command=prompt.destroy).grid(row=1, column=1, sticky="WE")

        #Center the prompt
        _center(prompt)

        #Save the prompt as an instance variable
        self._prompt = prompt

    def _open(self) :
        #Opens all shortcuts in the selected folders
        
        #Destroy old prompt
        self._prompt.destroy()
        
        #Get the current working directory, a.k.a the directory containing this script
        path = os.getcwd()
        
        #Run through each selected directory, and get all files inside each one
        for directory in self._selected :
            files = os.listdir(r'.\\' + directory.label)
            #Run through each file, using the system to run it
            for file in files :
                os.system('"' + path + '\\' + directory.label + '\\' + file + '"')
                
        #Destroy window upon completion
        self.destroy()

def _center(window) :
    #Centers 'window' in the screen
    
    #Ensure window size attributes are correct at time of centering
    window.update()
    
    #Get window size
    width = window.winfo_width()
    height = window.winfo_height()

    #Get screen size
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()

    #Calculate coordinates
    x = (screenwidth/2) - (width/2)
    y = (screenheight/2) - (height/2)

    #Set the dimensions of the window and its poisition
    window.geometry('%ix%i+%i+%i' %(width, height, x, y))
    
if __name__ == '__main__' :
    #Get the group folders
    cwd = '.'
    dirs = [os.path.join(cwd, o) for o in os.listdir(cwd) if os.path.isdir(os.path.join(cwd,o))]
    
    #Start the program
    window = EasyOpen(None)
    window.mainloop()

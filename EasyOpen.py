import os
import os.path
from tkinter import *
import re

#Get the names of all subdirectories, used for creating the checkboxes
#and for running the shortcuts in each group

##TK implementation
class EasyOpen(Tk) :
    #The main class of the window that will be used
    
    ##Class Constants
    #Title of the window
    _TITLE = 'EasyOpen v0.1'
    #Row to start placing widgets
    _ROW = 1

    def __init__(self, master, title=_TITLE) :
        #Run the super constructor
        Tk.__init__(self, master)
        #Set the title
        self.title(title)
        #Override default 'X' button command
        self.protocol('WM_DELETE_WINDOW', self._cancel)
        #Create a help label at the top
        Label(self, text="Select the groups to open and click Open").grid(row=0,
                                                        column=0, columnspan=2)
        #Initialise the checkboxes
        self._initialiseCheckboxes()
        #Initialise the confirm buttons
        self._initialiseButtons()
        #Remove resizability
        self.resizable(False, False)

    def _initialiseCheckboxes(self) :
        #Create the checkboxes using names of sibling folders
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
        #Createe and add cancel button
        cancel = Button(master=self, text="Cancel", command=self._cancel)
        cancel.grid(row=row, column=column, sticky=sticky)
        
    def _cancel(self) :
        #Display a new window prompting confirmation of cancellation   
        prompt = self._createPrompt()
        Label(master=prompt, text="Do you wish to cancel?").grid(row=0, column=0,
                                                        columnspan=2, sticky="WE")
        Button(master=prompt, text="Yes", command=self.destroy).grid(row=1, column=0,
                                                                     sticky="WE")
        Button(master=prompt, text="No", command=prompt.destroy).grid(row=1,column=1,
                                                                      sticky="WE")

    def _confirm(self) :
        #Display a new window showing the selected groups and prompt confirmation        
        global dirs
        prompt = self._createPrompt()
        selected = [checkbox for checkbox in self._checkboxes if checkbox.variable.get() == 1]
        dir_string = ''
        for checkbox in selected :
            if checkbox == selected[-1] :
                dir_string += checkbox.label
            else :
                dir_string += checkbox.label + '\n'
        self._selected = selected
        Label(master=prompt, text="You have selected the following groups:\n%s\nDo you wish to open these?" %(dir_string)).grid(row=0, column=0,
                                                        columnspan=2, sticky="WE")
        Button(master=prompt, text="Yes", command=lambda : self._open(prompt)).grid(row=1, column=0,
                                                                     sticky="WE")
        Button(master=prompt, text="No", command=prompt.destroy).grid(row=1,column=1,
                                                                      sticky="WE")
        
    def _createPrompt(self) :
        #Creates and returns a toplevel with application wide focus
        prompt = Toplevel()
        prompt.grab_set()
        prompt.title('')
        return prompt

    def _open(self, prompt) :
        #Opens all shortcuts in the selected folders
        #Destroy old prompt, create new giving progress report, then destroy everything
        prompt.destroy()
        prompt = self._createPrompt()
        var = StringVar()
        Label(prompt, text="Currently Opening:").grid(row=0,column=0)
        Label(prompt, textvariable=var).grid(row=0, column=1)
        path = os.getcwd()
        for directory in self._selected :
            var.set(directory.label)
            files = os.listdir(r'.\\' + directory.label)
            for file in files :
                os.system('"' + path + '\\' + directory.label + '\\' + file + '"')
        prompt.destroy()
        self.destroy()
    
if __name__ == '__main__' :
    #Get the folders
    d = '.'
    dirs = [os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]
    print(dirs)
    #Start the program
    window = EasyOpen(None)
    window.mainloop()

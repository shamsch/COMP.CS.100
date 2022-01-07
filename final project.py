"""
COMP.CS.100 Final Week Project
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program is a single window simple To-Do list GUI implemented program. You can add task, delete them, save them (stores in a .txt file locally), and load your tasks later.
It has some error handling implemented to circumvent some obvious error. I used some concepts which were not taught in the material such as scroll bar, message box, and listbox wideget.
It was inspired from a YouTube video that I watched. However, it's not copy pasted code. I am hoping it is considered as an advanced GUI in context of the project.

"""
# importing tkinter and messagebox

from tkinter import *
import tkinter.messagebox

#creating a class for the GUI

class UserInterface:

    #constructors

    def __init__(self):

        #launching tkinter and changing the title from default
        self.__mainwindow = Tk()
        self.__mainwindow.title("To Do List - by Shamsur")

        #creating a frame
        self.__taskFrame= Frame(self.__mainwindow)
        self.__taskFrame.pack()

        #adding a label
        self.__frameLabel = Label(self.__taskFrame, text="Your to do list:")
        self.__frameLabel.pack()

        #creating a scrollbar
        self.__scrollbar = Scrollbar(self.__taskFrame)
        self.__scrollbar.pack(side=RIGHT, fill=Y)

        #creating a listbox which will contain the tasks
        self.__listboxTasks= Listbox(self.__taskFrame, height=3, width=50)
        self.__listboxTasks.pack()

        #connecting the listbox and the scrollbar so that the scrollbar correspond to the listbox
        self.__listboxTasks.config(yscrollcommand=self.__scrollbar.set)
        self.__scrollbar.config(command= self.__listboxTasks.yview)

        #a simple label before the entry widget
        self.__entryLabel= Label(self.__mainwindow, text="Type your task below and add it:")
        self.__entryLabel.pack()

        #entry widget for task input
        self.__entryTask= Entry(self.__mainwindow,width=50)
        self.__entryTask.pack()

        #a button to add a task once it's been typed in the entry box
        self.__addTaskButton = Button(self.__mainwindow, text="Add Task", width= 48, command=self.add_task)
        self.__addTaskButton.pack()

        #a button to delete a task once the cursor selected the task from the listbox area of the GUI
        self.__deleteTaskButton = Button(self.__mainwindow, text="Delete Task", width=48, command=self.delete_task)
        self.__deleteTaskButton.pack()

        #a button to save all the tasks in order to a text file to retrieve later
        self.__saveTaskButton = Button(self.__mainwindow, text="Save Tasks", width=48, command=self.save_task)
        self.__saveTaskButton.pack()

        #a button to load all the task from the saved text file from the system in to listbox area of the GUI
        self.__loadTaskButton = Button(self.__mainwindow, text="Load Tasks", width=48, command=self.load_task)
        self.__loadTaskButton.pack()

        #a button to shutdown the GUI
        self.__stop_button = Button(self.__mainwindow, text="Stop", width=48, command=self.stop)
        self.__stop_button.pack()

    def add_task(self):
        """
        This method adds a task in the to-do list
        """
        #getting the string from the entry widget
        text = str(self.__entryTask.get())

        #if it's an empty string, raising a warning using message box
        if text == "":
            tkinter.messagebox.showwarning(title="Warning!!", message="Please enter a valid task")

        #otherwise inserting it into the display area of the GUI
        else:
            self.__listboxTasks.insert(END, text)
            #afterwards clearing the entry in preparation for a new user input
            self.reset_entry()

    def delete_task(self):
        """
        This method deletes the tasks selected by the user from the list box or display area of the GUI
        """
        #error handling implemented to make sure a task has been selected before deleting
        try:

            text = self.__listboxTasks.curselection()[0]
            self.__listboxTasks.delete(text)
        except:
            #raising a warning using message box in the case of no task selected before deleting
            tkinter.messagebox.showwarning(title="Warning!!", message="Please select a valid task to delete")

    def save_task(self):
        """
        This method saves the task presently displayed in listbox into a text file to retrieve later
        """
        # storing the text selected in variable
        text= self.__listboxTasks.get(0, END)
        #writing a text file
        textfile= open("finalproject_load.txt", mode= "w")
        for line in text:
            #passing the each line to the text file
            print(line, file=textfile)
        #closing the text file
        textfile.close()

    def load_task(self):
        """
        This method loads the tasks store previously from a text file
        """
        #error check to make sure there does indeed exist a saved file
        try:
            #reading a file
            file = open(file= "finalproject_load.txt", mode="r")
            #clearing the entire window so as to when load is pressed consecutively it does not create repetition
            self.__listboxTasks.delete(0, END)
            for fileline in file:
                fileline= fileline.rstrip()
                #inserting the file into the list box display area
                self.__listboxTasks.insert(END, fileline)
        except:
            #raising an error message
            tkinter.messagebox.showwarning(title="Warning!!", message="The program couldn't find a saved file")

    def reset_entry(self):
        """
        This method clears the entry area of the GUI
        """
        #delete everything from entry and leave an empty string
        self.__entryTask.delete(0, END)
        self.__entryTask.insert(0, "")

    def stop(self):
        """
        Ends the execution of the program.
        """
        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the execution of the program.
        """
        self.__mainwindow.mainloop()

def main():
    #storing the object
    runTheProgram= UserInterface()
    #calling a method
    runTheProgram.start()

if __name__ == "__main__":
    main()

#thank you for reading this through

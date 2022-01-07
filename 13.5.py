"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""

from tkinter import *


class Counter:
    def __init__(self):
        # TODO: You have to creater one label and four buttons and store
        #       them in the following attributes:
        #
        #       self.__current_value    # Label displaying the current value of the counter.
        #       self.__reset_button     # Button which resets counter to zero.
        #       self.__increase_button  # Button which increases the value of the counter by one.
        #       self.__decrease_button  # Button which decreases the value of the counter by one.
        #       self.__quit_button      # Button which quits the program.
        #
        #       Make sure you name the components exactly as shown above,
        #       otherwise the automated tests will fail.

        self.__main_window = Tk()
        self.__val=0

        self.__current_value = Label(self.__main_window, text=self.__val)
        self.__current_value.grid(row=0, column=0, columnspan= 4)

        self.__increase_button= Button(self.__main_window, text="Increase", command= self.increase_button)
        self.__increase_button.grid(row=1, column=0)

        self.__decrease_button= Button(self.__main_window, text="Decrease", command= self.decrease_button)
        self.__decrease_button.grid(row=1, column=1)

        self.__reset_button= Button(self.__main_window, text="Reset", command= self.reset_button)
        self.__reset_button.grid(row=1, column=2)

        self.__quit_button = Button(self.__main_window, text="Quit", command=self.quit_button)
        self.__quit_button.grid(row=1, column=3)


        self.__main_window.mainloop()

    # TODO: Implement the rest of the needed methods here.
    def quit_button(self):
        self.__main_window.destroy()
    def reset_button(self):
        self.__val=0
        self.__current_value.config(text= self.__val)
    def increase_button(self):
        self.__val+=1
        self.__current_value.config(text= self.__val)
    def decrease_button(self):
        self.__val-= 1
        self.__current_value.config(text= self.__val)



def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()


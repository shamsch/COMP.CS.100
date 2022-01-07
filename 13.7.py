"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""
from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        # TODO: Create an Entry-component for the weight.
        self.__weightLabel = Label(self.__mainwindow, text="Weight in KG")
        self.__weightLabel.pack()
        self.__weight_value = Entry(self.__mainwindow)
        self.__weight_value.pack()

        # TODO: Create an Entry-component for the height.
        self.__height_valueLabel= Label(self.__mainwindow, text="Height in CM")
        self.__height_valueLabel.pack()
        self.__height_value= Entry (self.__mainwindow)
        self.__height_value.pack()

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        #       the default colour.
        self.__calculate_button = Button(self.__mainwindow, text="Calculate", command= self.calculate_BMI, foreground="red")
        self.__calculate_button.pack()

        # TODO: Create a Label that will show the decimal value of the BMI
        #      after it has been calculated.
        self.__result_text = Label(self.__mainwindow, text="BMI will show here")
        self.__result_text.pack()


        # TODO: Create a Label that will show a verbal description of the BMI
        #       after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow, text= None)
        self.__explanation_text.pack()

        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow, text="Stop",
                                 command=self.stop)
        self.__stop_button.pack()

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        """self.__weight_value.grid()
        self.__height_value.grid()
        self.__calculate_button.grid()
        self.__stop_button.grid()
        self.__result_text.grid()
        self.__explanation_text.grid()"""

    # TODO: Implement this method.
    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """
        NegativeNUM= False
        try:
            height = float(self.__height_value.get())
            try:
                weight = float(self.__weight_value.get())
                if height<0 or weight<0:
                    NegativeNUM = True
                    raise ValueError
                bmi = weight / ((height / 100) * (height / 100))
                bmi_formatted= "{:.2f}".format(bmi)
                self.__result_text.configure(text=bmi_formatted)
                if bmi >= 18.5 and bmi <= 25.00:
                    self.__explanation_text.configure(text="Your weight is normal.")
                elif bmi > 25.00:
                    self.__explanation_text.configure(text="You are overweight.")
                else:
                    self.__explanation_text.configure(text="You are underweight.")
            except ValueError:
                self.reset_fields()
                if NegativeNUM:
                    self.__explanation_text.configure(text="Error: height and weight must be positive.")
                else:
                    self.__explanation_text.configure(text="Error: height and weight must be numbers.")
        except ValueError:
            self.reset_fields()
            self.__explanation_text.configure(text="Error: height and weight must be numbers.")



    # TODO: Implement this method.
    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """
        self.__result_text.configure(text="")

        self.__height_value.delete(0, END)
        self.__height_value.insert(0, "0")

        self.__weight_value.delete(0, END)
        self.__weight_value.insert(0, "0")

    def stop(self):
        """
        Ends the execution of the program.
        """
        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()

if __name__ == "__main__":
    main()

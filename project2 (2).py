"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program is assignment that takes electricity input and makes a histrogram. I did this on me own.

"""

def class_maximum_value(classno):
    """
    This function gets the maximum value in a class for the premade single line print function and return the max value
    """
    largest_value  = 10 ** classno - 1    # Given in the text description for this program
    return largest_value

def class_minimum_value(classno):
    """
    This function gets the minimum value in a class for the premade single line print function and returns the min value
    """
    smallest_value = 10 ** classno // 100 * 10  # Given in the text description for this program
    return smallest_value

def numberOfClass(arr):
    """
    This functiion takes a list input and finds how many class there needs to be
    """
    class_number =1
    maximum= max(arr) # Finding the biggest memember of the list
    while True:
        if class_minimum_value(class_number) <= maximum <= class_maximum_value(class_number): #This is just checking which
            break
        class_number+=1
    return class_number

def print_histogram(arr):
    """
    This function uses a new list to keep track of count in each class and then finally it passes the list systemically to the other single line print function
    """
    numOfClass=numberOfClass(arr) #Using the to find the largest class
    dataCount= [0] * (numOfClass+1) # Index 0 = 0 the rest would change, this is for ease of access later


    for val in arr:
        class_number = len(str(int(val))) # Using the fact that length of each number in the list is equal to the class which they belong (Logarthimatic property)
        dataCount[class_number]+=1 #Adding one to the class where the number belongs in our output list

    for i in range(1,len(dataCount)): # Running a loop to access each index of the newly created, skipping 0 since that's not relevant
        print_single_histogram_line(i,dataCount[i],len(dataCount)) # Passing the value systematically


def print_single_histogram_line(class_number, count, largest_class_number):
    """
    This function is probably the most challenging one in this assignment.
    It will print one correctly indented histogram line as described
    in the assignment instructions. Your job is to call it with
    correct parameters.

    :param class_number: int,
        Expresses which consumption class (1, 2, 3, ...)
        should the histogram line be printed for. The <class_number> is used
        to decide which value range (0-9, 10-99, 100-999, ...) should be
        printed in front of the histogram markers ("*").

    :param count: int,
        How many of the values entered by the user belong to <class_number>.

    :param largest_class_number: int,
        What is the largest class out of all input values
        the user entered. This is needed when deciding the indentations
        for all other histogram lines.  For example, if the largest
        number the user entered was 91827364 (8 digits) the value
        of this paramter should be 8.
    """

    # <range_string> represents the range of the values the line's
    # histogram will represent in the printout.  For example "1000-9999".
    # Uses the functions class_minimum_value and class_maximum_value which
    # have to be defined elsewhere.

    min_value = class_minimum_value(class_number)
    max_value = class_maximum_value(class_number)
    range_string = f"{min_value}-{max_value}"


    # How many characters will the largest class' range need when printed.
    # For example if the <largest_class_number> is 7, it would print
    # "1000000-9999999" in the beginning of the line and requires 15 characters.
    # This value defines the print width for all the other <range_string>'s.

    largest_width = 2 * largest_class_number - 1 #This is the only change I made, I did it bc +1 somehow was not working but -1 is, so this is bit of a hotfix


    # Now all the preparations have been done and we can print the
    # histogram line with the correct number of whitespaces in the
    # beginning of the line followed by the correct number of '*'
    # characters. ">" character in the following f-string places
    # <range_string>'s value to the right edge of the output field
    # (filler white spaces will be printed in the beginning).

    print(f"{range_string:>{largest_width}}: {'*' * count}")

def takeInput():
    """
    This function takes input for this problem and return a valid list
    """
    lst = [] # Declares an empty list
    while True:
        ele = input("Enter energy consumption (kWh): ") # Prompt
        if ele=="":
                break # Breaks if an empty string is returned
        elif int(ele)<0:
            print(f"You entered: {ele}. Enter non-negative numbers only!") # In the event of negative input
        else:
            lst.append(int(ele))  # Adding the element

    return lst # Returning the list


def main():
    print("Enter energy consumption data.")
    print("End by entering an empty line.")
    print()

    # Test values for the input data, so they don't have to be manually
    # entered every single time you want to test your program.  Before
    # submitting your program to Plussa these must be replaced by values
    # read from the user, otherwise the tests will fail.

    input_data = takeInput() #taking input

    if len(input_data)==0:
        print("Nothing to print. Done.") # If the list is empty
    else:
        print_histogram(input_data) # If not then we call the functions


if __name__ == "__main__":
    main()
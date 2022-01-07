"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""
def capitalize_initial_letters(string):
    """
    This function capitalize intial letter and returns it

    """

    i=""
    stringSplit= string.split()

    for val in stringSplit:
        i= i + val.capitalize() + " "

    j = i.rstrip()

    return j

def main():
    pass

if __name__ == "__main__":
    main()

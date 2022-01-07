"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""

def create_an_acronym(string):
    """
    this function takes a string input and retunrn
    """

    i=""
    stringSplit = string.split()
    for val in stringSplit:
        i= i + val[0]

    j= i.upper()
    return j

def main():
 pass

if __name__ == "__main__":
    main()

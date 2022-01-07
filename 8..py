"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""


def print_box(wS,hS,mark):
    """
    this is where the magic happens
    parameters are as followed width, height and the symbol
    """
    w=int(wS)
    h=int(hS)
    while h:
        x=w
        while x:
            print(mark, end="")
            if x==1:
                print()
            x=x-1
        h=h-1
def read_input(text):
    """
     this function takes input and returns it only if it is greater than zero and in the parameter you can put text you want to show with input
    """
    notValid= True
    while notValid:
        inputValue = input(text)
        try:
            returnVal = int(inputValue)
            notValid= False
        except ValueError:
            continue

    return returnVal
def main():
    x= read_input("Enter the width of a frame: ")
    y= read_input("Enter the height of a frame: ")
    z= input("Enter a print mark: ")
    print()
    print_box(x,y,z)


if __name__ == "__main__":
    main()

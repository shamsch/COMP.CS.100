"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program is printing a box with symbol user inputed

"""
def print_box(wS,hS,mark):
    """
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

def main():
    x= int(input("Enter the width of a frame: "))
    y= int(input("Enter the height of a frame: "))
    z= input("Enter a print mark: ")
    print()
    print_box(x,y,z)


if __name__ == "__main__":
    main()

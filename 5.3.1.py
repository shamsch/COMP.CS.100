"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""


def main():
    my_list = []
    print("Give 5 numbers:")
    x=5
    while x:
        val= int(input("Next number: "))
        my_list.append(val)
        x -= 1
    print("The numbers you entered that were greater than zero were:")
    for y in my_list:
        if y>0:
            print(y)


if __name__ == "__main__":
    main()

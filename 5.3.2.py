"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""


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

    y= len(my_list)-1
    print("The numbers you entered, in reverse order:")
    while y>-1:
        print(my_list[y])
        y-=1

if __name__ == "__main__":
    main()

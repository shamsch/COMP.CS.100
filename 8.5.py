"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""


def main():
    filename = input("Enter the name of the file: ")
    try:
        file = open(filename, mode="r")
    except OSError:
        print("There was an error in reading the file.")
        return

    number=0
    for file_line in file:
        number=number+1
        file_line = file_line.rstrip()
        print(number,file_line)

    file.close()


if __name__ == "__main__":
    main()

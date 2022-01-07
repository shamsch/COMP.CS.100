"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""



def main():
    filename = input("Enter the name of the file: ")

    try:
        save_file = open(filename, mode="w")

    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return

    print("Enter rows of text. Quit by entering an empty row.")
    number=0
    while True:
        text_line = input()
        if text_line == "":
            break
        number=number+1
        print(number,text_line, file=save_file)

    save_file.close()

    print(f"File {filename} has been written.")



if __name__ == "__main__":
    main()

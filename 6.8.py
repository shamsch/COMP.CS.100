"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program does something

"""
def isthereComma(str):
    """
    checks if there is any comma in the string if yes return true
    """
    for val in str:
        if val == ",":
            return True



def reverse_name(string):
    """"
    this is the function that reverses the name
    """
    if string=='':
        return string
    elif string==",":
        return ''
    elif isthereComma(string):
        x=string.split(",")
        lastName = x[0]
        firstName =  x[1]
        lastNameStrip= lastName.strip()
        firstNameStrip= firstName.strip()
        if firstNameStrip=="":
            return f"{lastNameStrip}"
        elif lastNameStrip=="":
            return f"{firstNameStrip}"
        else:
            return f"{firstNameStrip} {lastNameStrip}"
    else:
        return string
def main():
    pass

if __name__ == "__main__":
    main()

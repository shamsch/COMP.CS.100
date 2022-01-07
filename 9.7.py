"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""
def read_file(filename):
    """
    This function reads contacts from a CSV file and stuff
    """
    file = open(filename, mode="r")
    dictOne={}
    first_line= True
    for row in file:
        if first_line:
            key, name, phone, email, skype = row.rstrip().split(";")
            first_line = False
        else:
            str= row.rstrip().split(";")
            key1= str[0]
            name1=str[1]
            phone1=str[2]
            email1= str[3]
            try:
                skype1= str[4]
            except ValueError:
                skype1= None
            dictOne[key1]={}
            dictOne[key1][name]= name1
            dictOne[key1][phone]=phone1
            dictOne[key1][email]=email1
            dictOne[key1][skype]= skype1

    return dictOne


def main():
    pass

if __name__ == "__main__":
    main()

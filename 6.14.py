"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""

def count_abbas(string):
    """
    This function calculates abbas
    """
    count=0
    string= string + "   "

    for val in range(0,len(string)):
        if string[val] == 'a':
            if string[val+1] == 'b':
                if string[val+2]=='b':
                    if string[val+3]=='a':
                        count+=1


    return count

def main():
    pass

if __name__ == "__main__":
    main()

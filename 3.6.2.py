"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program is a song called Yogi Bear

"""
def repeat_name(name,timesStr):
    """
    This is the repeat name function which repeat names, parameter is  name and number repeats, no return value
    """
    times=int(timesStr)
    while times:
        print(name,", ", name," Bear",sep="")
        times = times -1

def verse(firstLine, secondLine):
    """
    This function uses anonther function to compose the verse of this song, parameter is the line and return value
    """
    print(firstLine)
    print(secondLine,", ",secondLine, sep="")
    print(firstLine)
    repeat_name(secondLine,3)
    print(firstLine)
    repeat_name(secondLine,1)
    print()
def main():
    verse("I know someone you don't know","Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend","Cindy")

if __name__ == "__main__":
    main()

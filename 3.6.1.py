"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""
def print_verse(x,y):
    """
    the function that prints the song
    :param x: name of the animal
    :param y: sound it makes
    """
    print("Old MACDONALD had a farm\nE-I-E-I-O\nAnd on his farm he had a ", x,"\nE-I-E-I-O", sep="")
    print("With a" , y,y,"here\nAnd a",y,y,"there")
    print("Here a ", y,", there a ", y,"\nEverywhere a ", y," ", y, sep="")
    print("Old MacDonald had a farm\nE-I-E-I-O")

def main():
    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")

if __name__ == "__main__":
    main()

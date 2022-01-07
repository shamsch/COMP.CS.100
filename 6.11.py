"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""


def encrypt(string):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    x=""

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    if string.isupper():
        stringLower = string.lower()
        for i in range(0,26):
            if stringLower==regular_chars[i]:
                x = encrypted_chars[i].upper()


    else:
        for i in range(0,26):
            if string==regular_chars[i]:
                x = encrypted_chars[i]

    if x== "":
        return string
    else:
        return x

def row_encryption(string):
    """
    this function perfoms a ROT13 transformation for an entire string
    """
    x=""
    for val in string:
        x+= encrypt(val)
    return x

def main():
    pass

if __name__ == "__main__":
    main()

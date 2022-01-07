"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program go through the characters of a string using a repeatition structure

"""


def main():
    word= input("Enter a word: ")
    vowel = 0
    consonant = 0
    for i in word:
        if i == 'a'or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vowel += 1
        else:
            consonant +=1
    print(f"The word {word} contains {vowel} vowels and {consonant} consonants")

if __name__ == "__main__":
    main()

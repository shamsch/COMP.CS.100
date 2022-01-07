"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    spanish_english = {}

    print("Dictionary contents:")
    i=""
    for val in sorted(english_spanish.keys()):
        i= i+", "+val

    j= i.strip(",")
    k= j.strip()
    print(k)

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            userIn= input("Enter the word to be translated: ")

            if userIn in english_spanish:
                print(f"{userIn} in Spanish is {english_spanish[userIn]}")
            else:
                print("The word", userIn, "could not be found from the dictionary.")

        elif command == "A":
            userInEng= input("Give the word to be added in English: ")
            userInEsp= input("Give the word to be added in Spanish: ")

            english_spanish[userInEng]= userInEsp

            print("Dictionary contents:")
            i = ""
            for val in sorted(english_spanish.keys()):
                i = i + ", " + val

            j = i.strip(",")
            k = j.strip()
            print(k)

        elif command == "R":
            userRemove= input("Give the word to be removed: ")
            if userRemove in english_spanish:
                del english_spanish[userRemove]
            else:
                print(f"The word {userRemove} could not be found from the dictionary.")

        elif command == "P":
            for keyS, valS in english_spanish.items():
                spanish_english[valS] = keyS
            print("\nEnglish-Spanish")
            for eng,esp in sorted(english_spanish.items()):
                print(eng,esp)
            print("\nSpanish-English")
            for esp, eng in sorted(spanish_english.items()):
                print(esp,eng)
            print()
        elif command == "T":
            userInTrans= input("Enter the text to be translated into Spanish: ")
            userOut=""
            x= userInTrans.split()
            for val in x:
                if val in english_spanish:
                    userOut= userOut + " " +english_spanish[val]
                else:
                    userOut= userOut + " " + val
            print("The text, translated by the dictionary: ")
            y= userOut.lstrip()
            print(y)

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()
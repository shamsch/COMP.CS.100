"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""
PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    while True:
        rawIn = input("Enter product name: ")
        userIn = rawIn.strip()
        if userIn == '':
            print('Bye!')
            break

        elif userIn not in PRICES:
            print(f"Error: {userIn} is unknown.")
        else:
            print(f"The price of {userIn} is {PRICES[userIn]:.2f} e")



if __name__ == "__main__":
    main()

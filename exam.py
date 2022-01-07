"""
COMP.CS.100 Exam
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program is created for the test

"""

LOAN_TIME = 3
MAX_LOANS = 3


class Librarycard:
    def __init__(self, card_id, card_holder):
        self.__id = card_id
        self.__holder = card_holder
        self.__loan=[]
        self.__weekcounter={}

    def id(self):
        return self.__id

    def holder(self):
        return self.__holder

    def info(self):
        print("Card holder:", self.__holder)
        if len(self.__loan)>0:
            self.__loan.sort()
            for var in self.__loan:
                print(f"- Loan {var}, loan time left {self.__weekcounter[var]} weeks")
        else:
            print("- No loans")

    def add_book(self, book):
        if len(self.__loan)<3:
            self.__loan.append(book)
            self.__weekcounter[book]=LOAN_TIME
            print(f"Loan successful, loan time {self.__weekcounter[book]} weeks")
        else:
            print(f"Card {self.__id} has already {MAX_LOANS} loans\nLoan not successful")

    def remove_book(self,book):
        self.__loan.remove(book)
        self.__weekcounter.pop(book)

    def update_week(self):
        for every in self.__weekcounter.keys():
            if self.__weekcounter[every]<=0:
                pass
            else:
                self.__weekcounter[every]-=1


def read_card_data(file_name):
    card_data = {}

    try:
        file_object = open(file_name, mode="r")

        for line in file_object:
            line = line.strip()
            strings = line.split(";")

            card_id = int(strings[0])
            card_holder = strings[1]

            new_card = Librarycard(card_id, card_holder)

            card_data[card_id] = new_card

    except OSError:
        print("Error in reading the file")
        return None

    return card_data


def read_card_id(prompt, database):
    while True:
        try:
            id = int(input(prompt))

            while id not in database:
                print("Erroneous card id, existing id's are:")
                listing(database)
                id = int(input(prompt))

            return id

        except ValueError:
            print("Erroneous card id, existing id's are:")
            listing(database)


def listing(cards):
    for card in sorted(cards):
        print(card, ":", cards[card].holder())

def generate_unique_values_in_dict(paradict):
    unique_val=[]
    for var in paradict.values():
        if var not in unique_val:
            unique_val.append(var)
    return unique_val

def main():
    library = read_card_data("library.txt")
    if library == None:
        return

    lended_book={}

    print("Welcome to Perähikiä library!")

    while True:
        command = input("Command: ")
        command = command.upper()

        if command == "I":
            card = read_card_id("Card code: ", library)
            library[card].info()

        elif command == "L":
            listing(library)

        elif command == "B":
            card = read_card_id("Card code: ", library)
            loan= input("Book code: ")
            if loan not in lended_book.keys():
                library[card].add_book(loan)
                lended_book[loan]=card
            else:
                card= lended_book[loan]
                print(f"Customer {library[card].id()} {library[card].holder()} has already borrowed book with id {loan}")

        elif command == "R":
            book_to_return= input("Book code: ")
            if book_to_return not in lended_book.keys():
                print("This book has not been borrowed by anyone")
            else:
                returners_id= lended_book[book_to_return]
                library[returners_id].remove_book(book_to_return)
                print("Book returned")
                lended_book.pop(book_to_return)


        elif command == "W":
            active_lenders=generate_unique_values_in_dict(lended_book)
            for every in active_lenders:
                library[every].update_week()

            print("Loan times updated!")

        elif command == "" or command == "Q":
            print("Thankyou and good bye!")
            return

        else:
            print("Erroneous command!")
            print("The commands are:")
            print("Info")
            print("List librarycards")
            print("Borrow")
            print("Return")
            print("new Week")


if __name__ == "__main__":
    main()

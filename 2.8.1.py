# COMP.CS.100 Week Chapter
# Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
# Student Number: 050359798

def main():
    month = 1
    date = 1
    monthEnd = True
    while month <= 12:
        monthEnd = True
        while monthEnd:
            if month<=7:
                if month == 2 and date <= 28:
                    print(date, ".", month, ".", sep="")
                elif month % 2 == 0 and month != 2 and date <= 30:
                    print(date, ".", month, ".", sep="")
                elif month % 2 != 0 and month != 2 and date <= 31:
                    print(date, ".", month, ".", sep="")
                else:
                    monthEnd = False
                    date = 0
                    month += 1
                date += 1
            else:
                if month % 2 != 0 and date <= 30:
                    print(date, ".", month, ".", sep="")
                elif month % 2 == 0 and date <= 31:
                    print(date, ".", month, ".", sep="")
                else:
                    monthEnd = False
                    date = 0
                    month += 1
                date += 1


if __name__ == "__main__":
    main()

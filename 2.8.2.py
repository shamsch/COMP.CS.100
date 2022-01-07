# COMP.CS.100 Week Chapter
# Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
# Student Number: 050359798

def main():
    day = 3
    month = 1
    loop= True
    while loop:
        if month == 1 and day > 31:
            day = day%31
            month = 2
        if month == 2 and day > 28:
            day= day%28
            month = 3
        if month == 3 and day > 31:
            day = day%31
            month = 4
        if month == 4 and day > 30:
            day = day%30
            month = 5
        if month == 5 and day > 31:
            day = day%31
            month = 6
        if month == 6 and day > 30:
            day = day%30
            month = 7
        if month == 7 and day > 31:
            day = day%31
            month = 8
        if month == 8 and day > 31:
            day = day%31
            month = 9
        if month == 9 and day > 30:
            day = day%30
            month = 10
        if month == 10 and day > 31:
            day = day%31
            month = 11
        if month == 11 and day > 30:
            day = day%30
            month = 12
        print(day, ".", month, ".", sep="")
        day += 7
        if month == 12 and day > 31:
            loop= False




if __name__ == "__main__":
    main()

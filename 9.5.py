"""
COMP.CS.100 Programming 1
Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.
"""

def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    TODO: comment the parameter and the return value.
    """

    dictOne= {}

    try:
        file = open(filename, mode="r")

        for row in file:

            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            for everyGen in genres:
                if everyGen not in dictOne:
                    dictOne[everyGen]=[]
                dictOne[everyGen].append(name)



        file.close()
        return  dictOne

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)
    str = ""

    for gen in sorted(genre_data.keys()):
        str = str + gen + ", "

    strFix= str.rstrip(", ")
    print("Available genres are:",strFix)

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        if genre in genre_data.keys():
            for val in sorted(genre_data[genre]):
                print(val)


if __name__ == "__main__":
    main()

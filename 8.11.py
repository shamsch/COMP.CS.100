"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""


def main():
    filename = input("Enter the name of the score file: ")
    try:
        file = open(filename, mode="r")
    except OSError:
        print("There was an error in reading the file.")
        return

    dictScore= {}
    for file_line in file:
        file_line= file_line.rstrip()
        try:
            file_lineSplit= file_line.split()
            scoreList= file_line.split(" ",2)
            nameOfContestant= scoreList[0]
            try:
                score= int(scoreList[1])
            except ValueError:
                print("There was an erroneous score in the file:")
                print(scoreList[1])
                return
            
        except IndexError:
            print("There was an erroneous line in the file:")
            print(file_line)
            return
        if nameOfContestant not in dictScore.keys():
            dictScore[nameOfContestant]= score
        else:
            dictScore[nameOfContestant]= dictScore[nameOfContestant]+score
    print("Contestant score:")
    for val in sorted(dictScore):
        print(val, dictScore[val])
    file.close()

if __name__ == "__main__":
    main()

# The third project of Programming 1 Spring 2021
# Name: Linh Nguyen
# Student ID: 050357952


class Ship:
    def __init__(self, ship_type, list, spacesOccupied):
        self.__ship_type = ship_type
        self.__coordinate_list = list
        self.__numberOfSquare = spacesOccupied

    def returnTheTypeOfTheShip(self):
        return self.__ship_type[0].upper()

    def returnTheCoordinateList(self):
        return self.__coordinate_list

    def attackedOnce(self):
        self.__numberOfSquare -= 1

    def returnOccupiedSpaces(self):
        return self.__numberOfSquare

    def returnTheShipName(self):
        return self.__ship_type


def generateAllOccupiedCoordinateList(listOfAllShip):
    occupiedCoordinate = []
    for ship in listOfAllShip:
        for coordinate in ship.returnTheCoordinateList():
            if coordinate not in occupiedCoordinate:
                occupiedCoordinate.append(coordinate)

    return occupiedCoordinate


def read_file(listOfAllShips):
    file_name = input("Enter file name: ")
    try:
        file = open(file_name, mode="r")
    except:
        print("File can not be read!")
        return False

    for line in file:
        line = line.strip()
        parts = line.split(";")

        typeOfTheShip = parts[0]
        coordinateList = []
        for number in range(1, len(parts)):
            y_coordinate = parts[number][0]
            if y_coordinate not in "ABCDEFGHIJ":
                print("Error in ship coordinates!")
                return False

            x_coordinate = parts[number][1]
            if x_coordinate not in "0123456789" or len(parts[number])>2:
                print("Error in ship coordinates!")
                return False

            occupiedCoordinate = generateAllOccupiedCoordinateList(listOfAllShips)

            if parts[number] in occupiedCoordinate:
                print("There are overlapping ships in the input file!")
                return False

            coordinateList.append(parts[number])

        spaceOccupied = len(coordinateList)
        ship = Ship(typeOfTheShip, coordinateList, spaceOccupied)
        listOfAllShips.append(ship)

    return True


def printBox(board, xCo=None, yCo=None, mark=""):
    print("")
    if xCo == None or yCo == None:
        for y in range(0, 12):
            if y > 0:
                print("")
            for x in range(0, 12):
                print(board[y][x], end=' ')
    else:
        for y in range(0, 12):
            if y > 0:
                print("")
            for x in range(0, 12):
                if x == xCo + 1 and y == yCo + 1:
                    board[y][x] = mark
                    print(board[y][x], end=' ')
                else:
                    print(board[y][x], end=' ')

    print("")
    print("")


def changeTheBox(board, x, y, shipType):
    board[y + 1][x + 1] = shipType


def checkIfValidCoordinateForPlay(board, x, y):
    if board[y + 1][x + 1] == ' ':
        return True
    else:
        return False


def whichShipIsThere(listOfShip, coordinate):
    for ship in listOfShip:
        occupiedSpaces = ship.returnTheCoordinateList()
        if coordinate in occupiedSpaces:
            return ship


def main():
    abortGame = False

    board = [
        [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', ' '],
        ['0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '0'],
        ['1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1'],
        ['2', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '2'],
        ['3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '3'],
        ['4', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '4'],
        ['5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '5'],
        ['6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '6'],
        ['7', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '7'],
        ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8'],
        ['9', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '9'],
        [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', ' '],

    ]

    letters_to_numbers = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'J': 9,

    }
    list_of_ships=[]

    if read_file(list_of_ships):
        printBox(board)
        while len(list_of_ships):
            entered_coordinate = input("Enter place to shoot (q to quit): ")

            if entered_coordinate == "q" or entered_coordinate == "Q":
                abortGame = True
                break
            if entered_coordinate==" " or entered_coordinate=="":
                print("Invalid command!")
                printBox(board)
            else:
                y_coordinate = entered_coordinate[0].upper()
                x_coordinate = entered_coordinate[1]

                allOccuppiedSpaces = generateAllOccupiedCoordinateList(list_of_ships)
                if y_coordinate not in "ABCDEFGHIJ" or x_coordinate not in "0123456789":
                    print("Invalid command!")
                    printBox(board)
                elif len(entered_coordinate)>2:
                    print("Invalid command!")
                    printBox(board)
                else:
                    row = letters_to_numbers[y_coordinate]
                    column = int(x_coordinate)
                    coordinate = y_coordinate + x_coordinate
                    if (checkIfValidCoordinateForPlay(board, row, column)):
                        if coordinate in allOccuppiedSpaces:
                            shipBeingAttacked = whichShipIsThere(list_of_ships, coordinate)
                            shipBeingAttacked.attackedOnce()
                            if shipBeingAttacked.returnOccupiedSpaces():
                                printBox(board, row, column, "X")
                            else:
                                for spaces in shipBeingAttacked.returnTheCoordinateList():
                                    xCor = int(spaces[1])
                                    yCor = letters_to_numbers[spaces[0]]
                                    changeTheBox(board, yCor, xCor, shipBeingAttacked.returnTheTypeOfTheShip())


                                print(f"You sank a {shipBeingAttacked.returnTheShipName()}!")
                                printBox(board)
                                list_of_ships.remove(shipBeingAttacked)

                        else:
                            printBox(board, row, column, "*")

                    else:
                        print("Location has already been shot at!")
                        printBox(board)

        if abortGame:
            print("Aborting game!")
        else:
            print("Congratulations! You sank all enemy ships.")



if __name__ == "__main__":
    main()


""""
COMP.CS.100 Programming 1 code template
Fill in all TODOs in this file
"""

from math import sqrt,pow


def menu():
    """
    This is a text-based menu. You should ONLY TOUCH TODOs inside the menu.
    TODOs in the menu call functions that you have implemented and take care
    of the return values of the function calls.
    """

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size,to_fill,gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas,x,y = drive(x,y,new_x,new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(size,gasFill, gasInTank):
    """
    This function has three parameters which are all FLOATs:
      (1) the size of the tank
      (2) the amount of gas that is requested to be filled in
      (3) the amount of gas in the tank currently

    The parameters have to be in this order.
    The function returns one FLOAT that is the amount of gas in the
    tank AFTER the filling up.

    The function does not print anything and does not ask for any
    input.
    """
    x= gasFill+gasInTank
    if x<=size:
        return x
    else:
        return size


def drive(currentX,currentY,destX,destY,gasInTank,gasConsump):
    """
    This function has six parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate
      (5) The amount of gas in the tank currently
      (6) The consumption of gas per 100 km of the car

    The parameters have to be in this order.
    The function returns three floats:
      (1) The amount of gas in the tank AFTER the driving
      (2) The reached (new) x coordinate
      (3) The reached (new) y coordinate

    The return values have to be in this order.
    The function does not print anything and does not ask for any
    input.
    """
    if currentX== 0 and currentY==0 and destX==0 and destY==0:
       return gasInTank, 0,0

    else:
        travelX=distance(currentX,destX)
        travelY= distance(currentY,destY)

        totalTravel= sqrt(travelX+travelY)
        gasLeft = gasInTank-(totalTravel * (gasConsump/100))

        possibleTravel = gasInTank * (100/gasConsump)

        delX= currentX+ (possibleTravel/totalTravel)*(destX-currentX)
        delY= currentY+ (possibleTravel/totalTravel)*(destY-currentY)

        if fuelCheck(totalTravel, gasConsump, gasInTank):
            return gasLeft, destX,destY

        else:
            return  0, delX, delY




def fuelCheck(travel, consump, inTank):
    """
    chekcs if travel is possible with the existing fuel

    """
    fuelNeed= travel * (consump/100)
    if fuelNeed<=inTank:
        return True
    else:
        return False




def distance(x1,x2):
    """
    calculates the distance

    """
    return pow(x2-x1,2)

def read_number(prompt, error_message="Incorrect input!"):
    """
    DO NOT TOUCH THIS FUNCTION.
    This function reads input from the user.
    Also, don't worry if you don't understand it.
    """

    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


if __name__ == "__main__":
    main()

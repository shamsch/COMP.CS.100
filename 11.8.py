"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""
class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __str__(self):
        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def __lt__(self, other):
        return (self.__numerator/self.__denominator) < (other.__numerator/other.__denominator)
    def __gt__(self, other):
        return (self.__numerator / self.__denominator) > (other.__numerator / other.__denominator)

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """
        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""
        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        gcm= greatest_common_divisor(self.__numerator,self.__denominator)
        self.__numerator= self.__numerator//gcm
        self.__denominator = self.__denominator//gcm

    def complement(self):
        x= self.__numerator
        y= self.__denominator

        if self.__numerator<0:
            return Fraction(-x,y)
        else:
            return Fraction(x,-y)

    def reciprocal(self):
        x = self.__numerator
        y = self.__denominator

        return Fraction(y,x)

    def multiply(self, object):
        num= self.__numerator* object.__numerator
        denom= self.__denominator* object.__denominator
        return Fraction(num, denom)

    def divide(self,object):
        num = self.__numerator * object.__denominator
        denom = self.__denominator * object.__numerator
        return Fraction(num, denom)

    def add(self, obj):
        a= int(self.__numerator)
        b= int(self.__denominator)
        c= int(obj.__numerator)
        d= int(obj.__denominator)
        num= (a*d)+(c*b)
        denom= (b*d)
        return Fraction(num, denom)

    def deduct(self, obj):
        a = int(self.__numerator)
        b = int(self.__denominator)
        c = int(obj.__numerator)
        d = int(obj.__denominator)
        num = (a * d) - (c * b)
        denom = (b * d)
        return Fraction(num, denom)

def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a

def add():
    """"
    this function adds
    """
    fracDict = {}
    userIn = str(input("Enter a fraction in the form integer/integer: "))
    userInSplit = userIn.split("/")
    num = int(userInSplit[0])
    denom = int(userInSplit[1])
    call = Fraction(num, denom)
    nameIn=input("Enter a name: ")
    fracDict[nameIn]=call

    return fracDict

def printOut(dict):
    """"
    this function prints
    """
    userIn=input("Enter a name: ")
    if userIn in dict.keys():
        print(f"{userIn} = {dict[userIn]}")
    else:
        print(f"Name {userIn} was not found")

def sortedList(dict):
    """
    this function sorts the list enter by the user
    """
    for var in sorted(dict.keys()):
        print(f"{var} = {dict[var]}")

def multiply(dict):
    """
    this function multiplies
    """
    userIn1=input("1st operand: ")
    if not userIn1 in dict.keys():
        print(f"Name {userIn1} was not found")
        return
    userIn2=input("2nd operand: ")
    if not userIn2 in dict.keys():
        print(f"Name {userIn2} was not found")
        return
    x= dict[userIn1]
    y= dict[userIn2]
    product = x.multiply(y)
    print(f"{dict[userIn1]} * {dict[userIn2]} = {product}")
    product.simplify()
    print(f"simplified {product}")

def readFile(dict):
    """
    this function reads file
    """
    filename = input("Enter the name of the file: ")
    try:
        file = open(filename, mode="r")
    except:
        print(f"Error: the file cannot be read.")
        return
    for file_line in file:
        file_line = file_line.rstrip()
        try:
            line= file_line.split("=")
            name=line[0]
            split= line[1].split("/")
            num = int(split[0])
            denom = int(split[1])
            call = Fraction(num, denom)
            dict[name]=call
        except:
            print(f"Error: the file cannot be read.")
            return 

def main():
    mainFracDict={}
    while True:
        userIn= input("> ")
        if userIn=="quit":
            print("Bye bye!")
            break
        elif userIn=="add":
            smth=add()
            mainFracDict.update(smth)
        elif userIn=="print":
            printOut(mainFracDict)
        elif userIn=="*":
            multiply(mainFracDict)
        elif userIn=="list":
            sortedList(mainFracDict)
        elif userIn=="file":
            readFile(mainFracDict)
        else:
            print("Unknown command!")

if __name__ == "__main__":
    main()

"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code template
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

"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program calculates the area of any triange

"""
from math import sqrt

def area(a,b,c):
    s=(a+b+c)/2
    x=(s-a)*(s-b)*(s-c)
    ar=sqrt(s*x)
    return ar

def main():
    firstSide = float(input("Enter the length of the first side: "))
    secondSide = float(input("Enter the length of the second side: "))
    thirdSide = float(input("Enter the length of the third side: "))
    areaOfTri= area(firstSide,secondSide,thirdSide)
    print(f"The triangle's area is {areaOfTri:.1f}")
if __name__ == "__main__":
    main()

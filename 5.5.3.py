"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program is for Rubik's cube


"""
def take_in():
    """
    takes input and returns a list
    """
    x=1
    list=[]
    while not x>5:
       y=float(input(f"Enter the time for performance {x}: "))
       list.append(y)
       x+=1
    return list

def main():
    userIn = take_in()
    theMax = max(userIn)
    theMin = min(userIn)
    userIn.remove(theMax)
    userIn.remove(theMin)
    run = 2
    sum=0
    while run>=0:
        x= userIn[run]
        sum = sum + x
        run -= 1
    avg= sum/3
    print(f"The official competition score is {avg:.2f} seconds.")


if __name__ == "__main__":
    main()

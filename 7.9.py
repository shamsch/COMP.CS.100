"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""
def takeInput():
    """"
    this function takes input for this program
    """
    print("Enter rows of text for word counting. Empty row to quit.")
    y=""
    while True:
        x=input()
        if x=="":
            break
        else:
            y=y+" "+ x.lower()
    return y

def main():
    userIn=takeInput()
    userInSplit= userIn.split()
    countDict={}

    for val1 in userInSplit:
        count=0
        for val2 in userInSplit:
            if val1==val2:
                count+=1
                countDict[val1]= count

    for keyS, valS in sorted(countDict.items()):
        print(f"{keyS} : {valS} times")

if __name__ == "__main__":
    main()

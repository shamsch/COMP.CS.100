"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program does something I am not very sure of

"""
def are_all_members_same(list):
    """
    this function takes a list as param and sees if all the values are the same
    """
    if len(list)==0:
        return True
    else:
        x= max(list)
        y= min(list)

        if x==y:
            return True
        else:
            return False



def main():
    pass

if __name__ == "__main__":
    main()

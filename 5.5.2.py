"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program

"""
def is_the_list_in_order(list):
    """
     this function works in a way
    """
    if len(list)>0:
        revList= list.copy()
        list.sort()
        if revList == list:
            return True
        else:
            return False
    else:
        return True


def main():
    pass

if __name__ == "__main__":
    main()

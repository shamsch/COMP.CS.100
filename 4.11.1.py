"""
COMP.CS.100 Week Chapter 
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

This program 

"""
def print_box(width,height,border_mark="#",inner_mark=" "):
    """
    this is where the magic happens
    parameters are as followed width, height and the symbol
    """
    w=int(width)
    h=int(height)
    while h:
        x=w
        while x:
            if x<w and h<height and not x==1 and not h==1:
                print(inner_mark, end="")
            else:
                print(border_mark, end="")
            if x==1:
                print()
            x=x-1
        h=h-1
    print()

def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)

if __name__ == "__main__":
    main()

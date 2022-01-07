""""
COMP.CS.100 Week 3 Project 1
Name: Shamsur Raza Chowdhury <shamsurraza.chowdhury@tuni.fi>
Student Number: 050359798

I did this group project on my own. This python program is basically a two player game called "game of sticks" where you have 21 sticks
and each player can remove 1 to 3 stick(s) in their turn. Last one to remove the stick loses.  

"""

def main():
    print("Game of sticks")
    stick = 21
    run_loop = True                         #this is our main loop variable
    counter=0                               #what this does is keep a count of whose turn is it
    while run_loop:

        if counter==0 or counter%2==0: #this if statement make sure it's either the first turn or player 1 turn
            player_1=int(input("Player 1 enter how many sticks to remove: ")) #taking player 1 input
            if player_1<1 or player_1>3:
                print("Must remove between 1-3 sticks!") #making sure it's a valid input, if not then the reminder and since rest of it won't run we'd come back here
                continue
            else:
                stick= stick - player_1 #deducting removed stick
                counter += 1 #registering player one entry
                if stick <= 0:
                    run_loop = False #making sure we are not at 0 or less sticks just yet
                else:
                    print(f"There are {stick} sticks left") #printing the number of stick left
                    player_2 = int(input("Player 2 enter how many sticks to remove: ")) #taking player two input
                    if player_2 < 1 or player_2 > 3: #the rest is same as above but for player 2 this time around
                        print("Must remove between 1-3 sticks!")
                    else:
                        stick = stick - player_2
                        counter += 1
                        if stick <= 0:
                            run_loop = False
                        else:
                            print(f"There are {stick} sticks left")
        else: #this else statement makes sure if player 2 inputs an invalid input we are asking giving him/her the turn, without it the turn would go to player one
            player_2 = int(input("Player 2 enter how many sticks to remove: "))
            if player_2 < 1 or player_2 > 3:
                print("Must remove between 1-3 sticks!")
            else:
                stick = stick - player_2
                counter += 1
                if stick <= 0:
                    run_loop = False
                else:
                    print(f"There are {stick} sticks left")

    if counter%2==0: #the counter here checks whose move was the last
        print("Player 2 lost the game!")
    else:
        print("Player 1 lost the game!") #evalutes who won






if __name__ == "__main__":
    main()

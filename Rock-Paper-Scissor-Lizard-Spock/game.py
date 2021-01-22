import random
import time
import sys
import os

# clearing screen function
def clear():

    if sys.platform in ["win32", "cygwin"]:
        os.system("cls")
    
    elif sys.platform in ["darwin", "linux"]: # clearing screen on mac or linux OS
        os.system("clear")

# rock-paper-scissor instructions
def rps_instructions():

    print()
    print("Instructions for Rock-Paper-Scissors : ")
    print()
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print()

# rock-paper-scissor-lizard-spock instructions
def rpsls_instructions():

    print()
    print("Instructions for Rock-Paper-Scissors-Lizard-Spock : ")
    print()
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print("Rock crushes Lizard")
    print("Lizard poisons Spock")
    print("Spock smashes Scissors")
    print("Scissors decapitates Lizard")
    print("Lizard eats Paper")
    print("Paper disproves Spock")
    print("Spock vaporizes Rock")
    print("Rock crushes Scissors")
    print()

# rock-paper-scissor game
def rps_game():

    global name

    # loop for endless playing
    while True:

        # all valid moves
        moves = ["rock", "paper", "scissor"]

        # menu of game
        print("-" * 36)
        print("\t\tMenu")
        print("-" * 36)
        print()
        print("Enter \"Help\" for instructions.")
        print("Enter \"Rock\", \"Paper\" or \"Scissor\" to play.")
        print("Enter \"Exit\" or press \"ctrl + c\" to go to main menu.")
        print()

        # user input
        user = input("Enter your move\n>>> ").lower()

        if user == "exit":  # go back to main menu
            clear()
            break

        elif user == "help":  # user wants to see instructions
            rps_instructions()
            continue

        elif user not in moves:  # check if invalid input then loop again
            print("Invalid input.\nTry Again.\n")
            continue

        # making computer's move
        comp = moves[random.randint(0, 2)]

        # simulating computer's move
        print("Computer making a move....")
        time.sleep(2)
        print()
        print("Computer chooses", comp.upper())
        print()

        # game comparisons
        if comp == user:
            print("Game TIED!")
            
        else:   # If game didn't tie
            
            # true value if the user won else false
            user_win = (user == "rock" and comp == "scissor") or (user == "paper" and comp == "rock") or (user == "scissor" and comp == "paper")

            if user_win:  # User Won
                print(name, " won.")
                print("Congratulations!")

            else:  # User Lost 
                print("Computer won.")
                print("Bad luck")

        # clearing the screen
        print()
        time.sleep(4)

# rock-paper-scissor-lizard-spock game
def rpsls_game():
    
    global name

    # loop for endless playing
    while True:

        # all valid moves
        moves = ["rock", "paper", "scissor", "lizard", "spock"]

        # menu of game
        print("-" * 52)
        print("\t\t\tMenu")
        print("-" * 52)
        print()
        print("Enter \"Help\" for instructions.")
        print("Enter \"Rock\", \"Paper\", \"Scissor\", \"Lizard\" or \"Spock\" to play.")
        print("Enter \"Exit\" or press \"ctrl + c\" to go to main menu.")
        print()

        # user input
        user = input("Enter your move\n>>> ").lower()

        if user == "exit":  # go back to main menu
            clear()
            break

        elif user == "help":  # user wants to see instructions
            rpsls_instructions()
            continue

        elif user not in moves:  # check if invalid input then loop again
            print("Invalid input.\nTry Again.\n")
            continue

        # making computer's move
        comp = moves[random.randint(0, 4)]

        # simulating computer's move
        print("Computer making a move....")
        time.sleep(2)
        print()
        print("Computer chooses", comp.upper())
        print()

        # game comparisons
        if comp == user:
            print("Game TIED!")
            
        else:   # If game didn't tie
            
            # true value if the user won else false
            user_win = (user == "rock" and comp in ["lizard", "scissor"]) or (user == "scissor" and comp in ["paper", "lizard"]) or (user == "paper" and comp in ["rock", "spock"]) or (user == "lizard" and comp in ["spock", "paper"]) or (user == "spock" and comp in ["rock", " scissor"])

            if user_win:  # User Won
                print(name, " Won.")
                print("Congratulations!")

            else:  # User Lost 
                print("Computer Won.")
                print("Bad luck!")

        # clearing the screen
        print()
        time.sleep(4)

# to input is user wants to play again
def replay():

    while True:

        inp = input("Do you want to play again? (yes or no)\n>>> ")
        
        if inp.lower()[0] not in ['y' or 'n']:
            continue
        
        return inp.lower()[0] == 'y'


# Main Game
GAME_ON = True

name = input("Your name\n>>> ")

while GAME_ON:

    # The Game Menu
    print()
    print("Let's Play!!!")
    print("Which version of Rock-Paper-Scissors?")
    print("Enter 1 to play Rock-Paper-Scissors")
    print("Enter 2 to play Rock-Paper-Scissors-Lizard-Spock")
    print("Enter 3 to quit")
    print()

    # Try block to handle the player choice 
    try:
        choice = int(input("Enter your choice = "))
    except ValueError:
        clear()
        print("Wrong Choice")   
        continue

    if choice == 1:
        rps_game()

    elif choice == 2:
        rpsls_game()

    elif choice == 3:
        break

    else:
        clear()
        print("Wrong choice. Read instructions carefully.")
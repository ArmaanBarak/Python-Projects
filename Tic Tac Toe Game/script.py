# Tic Tac Toe Game
# This is a multiplayer command line based game.
# Rules similar to original tic tac toe
# Made by: Armaan Barak

# Importing necessary functions
from os import name, system
from random import randint


# function to clear output
def clear_output():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


# function to display board
def display_board(board):

    clear_output()
    
    # printing board
    print('     |     |     ')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] + '  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] + '  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] + '  ')
    print('     |     |     ')


# function to select marker ('X' or 'O')
def marker_choice():
    
    mark = ''
    
    # getting valid markers
    while mark not in ['X', 'O']:
        
        mark = input('Player 1: Enter your desired marker (X - O): ')
        
        if mark not in ['X', 'O']:
            
            print('Invalid Input!\nRetry: ')
    
    # returning markers
    if mark == 'X':
        return ('X', 'O')
    
    return ('O', 'X')


# function to set marker at given position
def set_marker(board, marker, position):
    
    board[position] = marker


# randomly decide which player will go first
def random_choice():
    
    if randint(0, 1) == 1:
        return 'Player 1'
    return 'Player 2'


# function to check if desired position is empty or not
def space_check(board, position):
    
    # return true if position is empty
    return board[position] == ' '


# function to check if full board is filled
def full_board_check(board):
    
    # loop to confirm every position is empty using space_check() function
    for i in range(1, 10):
        
        # if any position is empty return false
        if space_check(board, i):
            return False
    
    # If full board is filled then return true
    return True


# function to check if someone won
def win_or_not(board, mark):
    
    # Horizontal combinations check
    horizontal_1 = board[1] == mark and board[2] ==  mark and board[3] == mark
    horizontal_2 = board[4] == mark and board[5] ==  mark and board[6] == mark
    horizontal_3 = board[7] == mark and board[8] ==  mark and board[9] == mark
    
    # Vertical combinations check
    vertical_1 = board[1] == mark and board[4] ==  mark and board[7] == mark
    vertical_2 = board[2] == mark and board[5] ==  mark and board[8] == mark
    vertical_3 = board[3] == mark and board[6] ==  mark and board[9] == mark
    
    # Diagnol combinations check
    diagnol_1 = board[1] == mark and board[5] ==  mark and board[9] == mark
    diagnol_2 = board[3] == mark and board[5] ==  mark and board[7] == mark
    
    # pattern match check
    pattern_matched = horizontal_1 or horizontal_2 or horizontal_3 or vertical_1 or vertical_2 or vertical_3 or diagnol_1 or diagnol_2
    
    # returning final value
    return pattern_matched


# function to get desirable position from player to fill marker
def player_choice(board):
    
    index = None
    is_empty = False
    
    # taking input untill valid position is passed in and return valid position index
    while not is_empty:
        
        index = input('Enter desired position (1 - 9): ')
        
        if index not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            
            print('Invalid position!\nRetry: ')
            
        else:
            
            index = int(index)
            
            if space_check(board, index):
                
                return index
            
            else:
                
                print('Position Occupied!\nRetry: ')


# function to check if players want to play again
def replay():
    
    choice = ''
    
    # get input untill player enters Y or N
    while choice not in ['Y', 'N']:
        
        choice = input('Do you want to play again (Y - N): ')
        
        if choice not in ['Y', 'N']:
            
            print('Invalid Input!\nRetry: ')
    
    # return true if want to replay
    if choice == 'Y':
        return True
    return False


# If current file is run the play game
if __name__ == "__main__":

    # welcome message
    print('Welcome to Tic Tac Toe Game!')


    ### Main  Game Loop
    while True:
        
        # Creating board
        board = [' '] * 10

        # Dispalying board
        display_board(board)

        # Assigning markers
        player1_marker, player2_marker = marker_choice()

        # Assigning turns
        turn = random_choice()
        print(turn + ' will go first!')

        
        ## Asking if the players are ready to play
        ready = input('Are you ready to play? (Y - N): ')
        if ready.upper() == 'Y':
            game_on = True
        else:
            game_on = False
            break

        
        # Looping the game functions
        while game_on:

            #### PLAYER 1 TURN
            if turn == 'Player 1':

                # Displaying board again
                display_board(board)
                
                # Asking for position
                position = player_choice(board)
                
                # Updating the board and setting markers
                set_marker(board, player1_marker, position)

                ## Checking if Player 1 won or if the game tied
                if win_or_not(board, player1_marker):

                    display_board(board)
                    print('PLAYER 1 WON THE GAME!!')
                    game_on = False

                else:

                    if full_board_check(board):

                        print('GAME TIED!!')
                        break
                    else:
                        turn = 'Player 2'


            ### PLAYER 2 TURN
            else:
                
                # Displaying board
                display_board(board)
                
                # Asking for position
                position = player_choice(board)
                
                # Updating the board and setting markers
                set_marker(board, player2_marker, position)

                ## Checking if Player 2 won or if the game tied
                if win_or_not(board, player2_marker):

                    display_board(board)
                    print('PLAYER 2 WON THE GAME!!')
                    game_on = False
                    
                else:
                    if full_board_check(board):

                        print('GAME TIED!!')
                        break
                    else:
                        turn = 'Player 1'


        ## If they do not want to play again then break out of the loop
        if not replay():
            break


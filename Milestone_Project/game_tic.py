import random


def display_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])

def player_input():

    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Enter your choice X or O : ")

    if marker == 'X' : 
        return ('X' , 'O')
    else:
        return ('O' , 'X')
    

def place_marker(board, marker, position):
    board[position] = marker

    return board

def win_check(board , mark):
    # all rows
    # all columns
    # all diagonals

    return (
       (board[1] == board[2] == board[3] == mark) or 
       (board[4] == board[5] == board[6] == mark) or 
       (board[7] == board[8] == board[9] == mark) or 

       (board[1] == board[4] == board[7] == mark) or 
       (board[2] == board[5] == board[8] == mark) or 
       (board[3] == board[6] == board[9] == mark) or 

       (board[1] == board[5] == board[9] == mark) or 
       (board[7] == board[5] == board[3] == mark) )


def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board , position):
    return board[position] == ' '


def full_board_check(board):
    print((' ' not in board))
    print("-----:::: ")
    return ' ' not in board

def player_choice(board):

    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] and space_check(board,position):
        position = int(input("Enter choice from (1-9) : "))

    return position

def replay():
    choice = input("Play Again Yes ot No ")
    return choice == 'Yes'


# game running
print("Welcome Tic tac too....")
while  True:
    # set board , hwo is first. & which marker 
    board = [' '] * 10
    

    player1_marker  ,player2_marker = player_input()
    print(f"Player1 : {player1_marker}")
    print(f"Player2 : {player2_marker}")

    turn = choose_first()
    print(f"{turn} will go first")

    play_game = input("Ready to play game (y or n ) : ")
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # show baord
            display_board(board)
            print("--------")

            #get choice of posiiton
            position = player_choice(board)

            #place nmarker
            place_marker(board,player1_marker , position)

            if win_check(board , player1_marker):
                display_board(board)
                print("Player1 has won!..... ")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Tie Game....")
                    game_on = False
                else: 
                    turn = 'Player 2'
                    


        else:
            #player 2 turn
                        # show baord
            display_board(board)

            #get choice of posiiton
            position = player_choice(board)

            #place nmarker
            place_marker(board,player2_marker , position)

            if win_check(board , player2_marker):
                display_board(board)
                print("Player2 has won!..... ")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Tie Game....")
                    game_on = False
                else: 
                    turn = 'Player 1'






    if not replay():
        break
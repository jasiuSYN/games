def display_board(board):
    print('\n'*100)
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return('O','X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or # top line
    (board[4]==mark and board[5]==mark and board[6]==mark) or # mid line
    (board[7]==mark and board[8]==mark and board[9]==mark) or # bot line
    (board[1]==mark and board[4]==mark and board[7]==mark) or # col left
    (board[2]==mark and board[5]==mark and board[8]==mark) or # col mid
    (board[3]==mark and board[6]==mark and board[9]==mark) or # col right
    (board[1]==mark and board[5]==mark and board[9]==mark) or # x
    (board[3]==mark and board[5]==mark and board[7]==mark)) # x

import random

def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    if board[position] == ' ':
        return True

def full_board_check(board):
    for x in range(1,10):
        if space_check(board, x):
           return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Your next posiotion (1-9)?: '))
    
    return position
    
def replay():
        return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:    
    new_board = [' ']*10 #plansza
    
    player1_marker, player2_marker = player_input() #wybierz X albo O

    player = choose_first() #kto pierwszy
    print(player+' starts first!')

    play_game = input('Do you wan to start the game? "Y" or "N"? ').upper() #czy zacząć grę

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    #pass

    while game_on:
        if player == 'Player 1':
            # Player1's turn.
            
            display_board(new_board)
            position = player_choice(new_board)
            place_marker(new_board, player1_marker, position)

            if win_check(new_board, player1_marker):
                display_board(new_board)
                print(f'Congratulations! {player} have won the game!\n')
                game_on = False
            else:
                if full_board_check(new_board):
                    display_board(new_board)
                    print('The game is a draw!')
                    break
                else:
                    player = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(new_board)
            position = player_choice(new_board)
            place_marker(new_board, player2_marker, position)

            if win_check(new_board, player2_marker):
                display_board(new_board)
                print(f'Congratulations! {player} have won the game!\n')
                game_on = False
            else:
                if full_board_check(new_board):
                    display_board(new_board)
                    print('The game is a draw!')
                    break
                else:
                    player = 'Player 1'

    if not replay():
        break
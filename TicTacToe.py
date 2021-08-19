

def show_board(board):
    print('_' * 20)
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-' * 5)
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-' * 5)
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('_' * 5)


def check_for_winner(player_selections, player_turn, off_player):
    # feed in either player's board moves and check if contents in winning list
    for x in winning_solutions:
        if all(y in player_selections for y in x):
            print(f'{player_turn.upper()} wins!\n')
            return True
    # check for tied match
    if len(player_selections) > len(off_player) and len(player_selections) == 5:
        print('Tied game.')
        return True


def place_move(playing_board, example_board, player_turn, off_player):
    while True:
        print('===== Board Configuration ======')
        show_board(example_board)
        print('='*20)
        # make sure to feed which selections will be compared below when checking for a winner
        if player_turn == 'x':
            player_selections = x_selections
            off_player = o_selections
        else:
            player_selections = o_selections
            off_player = x_selections
        # ask for player input
        try:
            move = input(f'Where would you like to place your {player_turn} token? Choose a number 1-9:')
            if playing_board[move] == ' ':
                playing_board[move] = player_turn
                player_selections.append(move)
            else:
                print('That move is already taken. Try again.')
                # if gets to here, the code will have swapped turns from x to o, so swap it back.
                if player_turn == 'o':
                    player_turn = 'x'
                else:
                    player_turn = 'o'
        except KeyError:
            print('Not a valid selection. Try again.')
        show_board(original_board)
        # check for a winner, if so ask to play again
        if check_for_winner(player_selections, player_turn, off_player):
            response = input('Would you like to play again?')
            if response.lower().startswith('y'):
                return True
            else:
                return False
        # swap turns
        if player_turn == 'x':
            player_turn = 'o'
        else:
            player_turn = 'x'


def start_game():
    # main loop
    while True:
        print('Welcome to Tic Tac Toe!')
        print('='*20)
        print('X will go first.')
        # begin with player x and feed into place_move()
        player_turn = 'x'
        off_player = o_selections
        if place_move(playing_board=original_board,
                      example_board=board_config, player_turn=player_turn, off_player=off_player):
            # if returns true, clean up the board and clear out player selections for new game
            for key in original_board:
                original_board[key] = ' '
            o_selections.clear()
            x_selections.clear()
            continue
        # if any answer other than yes is given, will hit next line and end game
        return False


x_selections = []
o_selections = []
winning_solutions = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
                     ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
                     ['1', '5', '9'], ['3', '5', '7']]
board_config = {
    '1': '1', '2': '2', '3': '3',
    '4': '4', '5': '5', '6': '6',
    '7': '7', '8': '8', '9': '9',
}

original_board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' ',
}

start_game()

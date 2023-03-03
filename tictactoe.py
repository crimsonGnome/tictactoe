"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if(terminal):
        # Check if X or O wone 
        for row, i in enumerate(board):
        
            # 1) row check
            if row[0] == row[1] == row[2] == 'X': return 'X'
            if row[0] == row[1] == row[2] == 'O': return 'O'

            for space, j in enumerate(row):
                # 2) column check
                if i == 1:
                    if board[i-1][j] == board[i][j] == board[i+1][j] == 'X': return 'X'
                    if board[i-1][j] == board[i][j] == board[i+1][j] == 'O': return 'O'

        # Check both the x and O diagonals 
        if board[0][0] == board[1][1] == board[2][2] == 'X': return 'X'
        if board[0][0] == board[1][1] == board[2][2] == 'O': return 'O'
        if board[0][2] == board[1][1] == board[2][0] == 'X': return 'X'
        if board[0][2] == board[1][1] == board[2][0] == 'O': return 'O'

        return 'None'

    # Only  returns if there is no Terminal State
    return 'None'



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # defulat var
    emptySpace = False

    # 4 checks
    # 1) check if each row is matches
    # 2) check if each column matches
    # 3) check if there are no empty spaces
    # 4) check the two diagonals]]

    for i, row in enumerate(board):
        
        # 1) row check
        if row[0] == row[1] == row[2] != EMPTY: return True
    
        for j, space in enumerate(row):
            # change to false if there is an empty space
            if space == EMPTY:
                emptySpace = True

            # 2) column check
            if i == 1:
                if board[i-1][j] == board[i][j] == board[i+1][j] != EMPTY: return True
        
    
    # 3) return if there were no empty spaces 
    if emptySpace == False: return True

    # 4) check the diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY: return True
    if board[0][2] == board[1][1] == board[2][0] != EMPTY: return True

    # if no conditions met return False
    return False

    raise NotImplementedError


def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """



    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

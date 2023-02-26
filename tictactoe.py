"""
Tic Tac Toe Player
"""

import math
import copy

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
    # takes "board" and "action" as input
    # returns a new BOARD STATE (not actually modifying board)
    try:
        result = copy.deepcopy(board)
        # let player decide their next move based on action (input)
        result[action[0]][action[1]] = player(board)

        return result
    
    # if the action is not valid for the board, then raise an exception
    except:
        raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # defulat var
    emptySpace == False

    # 4 checks
    # 1) check if each row is matches
    # 2) check if each column matches
    # 3) check if there are no empty spaces
    # 4) check the two diagonals]]

    for row, i in enumerate(board):
        
        # 1) row check
        if row[0] == row[1] == row[2] != EMPTY: return True
    
        for space, j in enumerate(row):
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
    if board[0[2]] == board[1][1] == board[0][2] != EMPTY: return True

    # if no conditions met return False
    return False

    raise NotImplementedError


def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # accepts board as input
    # runner.py already checks if board is at terminal state
    try:
        
        if winner(board) == X:
            return 1
        if winner(board) == O:
            return -1
        # if game ends in a tie, return 0
        return 0
        
    except:
        raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

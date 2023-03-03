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
    # go through the board and count the number of X's and O's
    # if there are more X's on the board -> return O
    # if there are more O's on the board -> return X

    num_of_x = 0
    num_of_o = 0

    for r in range(0,len(board)):
        for c in range(0, len(board[0])):
            if board[r][c] == X:
               num_of_x += 1
            elif board[r][c] == O:
               num_of_o += 1

    if num_of_o >= num_of_x:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # if a spot is open or ("EMPTY") on the board 
    # fill in the open spot on the board

    # set of possible actions, each action is a tuple 
    possible_actions = set()

    for r in range(0,len(board)):
        for c in range(0, len(board[0])):
            if board[r][c] == EMPTY:
                possible_actions.add((r, c))
            
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
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

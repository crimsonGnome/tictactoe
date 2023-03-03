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

# note: minimax will directly call terminal(), score(), player(), actions()
# minimax will indirectly call result() from calling actions()
# minimax will need all other functions implemented before working

# def minimax(board):
    # return minimaxHelper(board, alpha, beta)

# def minimaxHelper(board, alpha, beta)
    # base case: leaf node, just returns 1, 0, or -1
    # if terminal(board)
        # return score(board)
    
    # recursive case
    # if !player(board)  # we are the ai and want to win; max value
        # maxEval = -infinity
        # for each branch of actions(board)
            # eval = minimaxHelper(branch, alpha, beta)
            # maxEval = max(maxEval, eval)
            # alpha =  max(alpha, eval)
            # if beta <= alpha
                # break
        # return maxEval

    # else  # we are viewing the player; player wants min value for us
        # for each branch of actions(board)
            # eval = minimaxHelper(branch, alpha, beta)
            # minEval = min(minEval, eval)
            # beta = min(beta, eval)
        # return minEval
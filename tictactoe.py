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

    # the ai is the current player() so we know what letter 'X' or 'O' it is
    # if ai is 'X' we want the final score to be 1 (max)
    # if ai is '0' we want the final score to be -1 (min)
    # use math library: infinity = math.inf, -infinity = -math.inf

    infinity = math.inf

    if player(board) == 'X':
        return minimaxHelper(board, -infinity, infinity, True)
    else:
        return minimaxHelper(board, -infinity, infinity, False)

def minimaxHelper(board, alpha, beta, maximizingPlayer):

    # base case: leaf node, just returns 1, 0, or -1
    if terminal(board):
        return score(board)
    
    # recursive cases
    infinity = math.inf

    if maximizingPlayer:
        maxEval = -infinity
        for branch in actions(board):
            eval = minimaxHelper(result(board, branch), alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha =  max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval

    else:
        minEval = infinity
        for branch in actions(board):
            eval = minimaxHelper(result(board, branch), alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval
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
    if(terminal):
        # Check if X or O won
        for i, row in enumerate(board):
        
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

    # Only returns if there is no Terminal State
    return 'None'



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # default var
    emptySpace = False

    # 4 checks
    # 1) check if each row is matches
    # 2) check if each column matches
    # 3) check if there are no empty spaces
    # 4) check the two diagonals

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
    if board[0][2] == board[1][1] == board[0][2] != EMPTY: return True

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
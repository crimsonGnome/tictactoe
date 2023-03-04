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
        print(result)
        return result
    
    # if the action is not valid for the board, then raise an exception
    except:
        raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # 1) Row check
    if board[0][0] == board[0][1] == board[0][2] == 'X': return 'X'
    if board[0][0] == board[0][1] == board[0][2] == 'O': return 'O'
    if board[1][0] == board[1][1] == board[1][2] == 'X': return 'X'
    if board[1][0] == board[1][1] == board[1][2] == 'O': return 'O'
    if board[2][0] == board[2][1] == board[2][2] == 'X': return 'X'
    if board[2][0] == board[2][1] == board[2][2] == 'O': return 'O'

    # 2) Column check
    if board[0][0] == board[1][0] == board[2][0] == 'X': return 'X'
    if board[0][0] == board[1][0] == board[2][0] == 'O': return 'O'
    if board[0][1] == board[1][1] == board[2][1] == 'X': return 'X'
    if board[0][1] == board[1][1] == board[2][1] == 'O': return 'O'
    if board[0][2] == board[1][2] == board[2][2] == 'X': return 'X'
    if board[0][2] == board[1][2] == board[2][2] == 'O': return 'O'

    # 3) Diagonals
    if board[0][0] == board[1][1] == board[2][2] == 'X': return 'X'
    if board[0][0] == board[1][1] == board[2][2] == 'O': return 'O'
    if board[0][2] == board[1][1] == board[2][0] == 'X': return 'X'
    if board[0][2] == board[1][1] == board[2][0] == 'O': return 'O'

    # No terminal state, return None
    return 'None'



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # 1) Row check
    if board[0][0] == board[0][1] == board[0][2] != EMPTY: return True
    if board[1][0] == board[1][1] == board[1][2] != EMPTY: return True
    if board[2][0] == board[2][1] == board[2][2] != EMPTY: return True

    # 2) Column check
    if board[0][0] == board[1][0] == board[2][0] != EMPTY: return True
    if board[0][1] == board[1][1] == board[2][1] != EMPTY: return True
    if board[0][2] == board[1][2] == board[2][2] != EMPTY: return True

    # 3) Diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY: return True
    if board[0][2] == board[1][1] == board[2][0] != EMPTY: return True

    # No conditions met, return False
    return False



def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # accepts board as input
    # runner.py already checks if board is at terminal state
    try:
        
        if winner(board) == 'X':
            return 1
        if winner(board) == 'O':
            return -1
        # if game ends in a tie, return 0
        return 0
        
    except:
        raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # note: the ai is either letter 'X' or 'O'
    # we want the player to lose! >:)
    # use math library: infinity = math.inf, -infinity = -math.inf

    if terminal(board):
        return None

    bestMove = (1, 1)

    if player(board) == 'X':
        bestScore = -math.inf
        for branch in actions(board):
                score = minimaxHelper(board, 0, -math.inf, math.inf, False)
                if score > bestScore:
                    bestMove = branch
    else:
        bestScore = math.inf
        for branch in actions(board):
            score = minimaxHelper(board, 0, -math.inf, math.inf, True)
            if score < bestScore:
                bestMove = branch
        
    return bestMove

def minimaxHelper(board, depth, alpha, beta, maximizingX):
    # base case: leaf node, just returns 1 (X wins), 0 (draw), or -1 (O wins)
    # reminder: the ai is trying to get the best score possible
    if terminal(board):
        return score(board)
    
    # recursive cases

    # X's turn, maximize score
    if maximizingX:
        bestValue = -math.inf
        for branch in actions(board):
            value = minimaxHelper(result(board, branch), depth + 1, alpha, beta, False)
            if value > bestValue:
                bestValue = value - depth * 10
            alpha = max(alpha, bestValue)
            if beta <= alpha:
                break
        return bestValue

    # O's turn, minimize score
    else:
        bestValue = math.inf
        for branch in actions(board):
            value = minimaxHelper(result(board, branch), depth + 1, alpha, beta, True)
            if value < bestValue:
                bestValue = value + depth * 10
            beta = min(beta, bestValue)
            if beta <= alpha:
                break
        return bestValue
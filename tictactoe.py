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
    
    # Loop through and count x and o
    for r, row in enumerate(board):
        for c, space in enumerate(row):
            if board[r][c] == 'X':
               num_of_x += 1
            elif board[r][c] == 'O':
               num_of_o += 1

    # if O > X then return
    if num_of_o >= num_of_x:
        return 'X'
    else:
        return 'O'


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
        if(player(board) == 'X'):
            result[action[0]][action[1]] = "X"
        else: 
            result[action[0]][action[1]] = "O"

        return result
    
    # if the action is not valid for the board, then raise an exception
    except:
        raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if(terminal):
        # Check if X or O wone 
        for i, row in enumerate(board):
        
            # 1) row check
            if row[0] == row[1] == row[2] == 'X': return 'X'
            if row[0] == row[1] == row[2] == 'O': return 'O'

            for j, space in enumerate(row):
                # 2) column check
                if i == 1:
                    if board[0][j] == board[1][j] == board[2][j] == 'X': return 'X'
                    if board[0][j] == board[1][j] == board[2][j] == 'O': return 'O'

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

    # note: the ai is either letter 'X' or 'O'
    # we want the player to lose! >:)
    # use math library: infinity = math.inf, -infinity = -math.inf
    
    # return if board is full
    if terminal(board):
        return None

    bestMove = (1, 1)

    # Determine who we are playing as
    if player(board) == 'X':
        # start off beste score as negative infinity (best)
        bestScore = -math.inf
        # loop through to find maximum score
        for branch in actions(board):
                score = minimaxHelper(result(board, branch), False)
                if score > bestScore:
                    bestScore = score
                    bestMove = branch
    else:
        # start off beste score as infinity (worst)
        bestScore = math.inf
        # loop through to find minimum score
        for branch in actions(board):
            score = minimaxHelper(result(board, branch), True)
            if score < bestScore:
                bestScore = score
                bestMove = branch
        
    return bestMove

def minimaxHelper(board, maximizingX):
    # base case: leaf node, just returns 1 (X wins), 0 (draw), or -1 (O wins)
    # reminder: the ai is trying to get the best score possible
    if terminal(board):
        return score(board)
    
    # recursive cases

    # X's turn, maximize score
    if maximizingX:
        bestScore = -math.inf 
        # find the hightest value and return
        for branch in actions(board):
            value = minimaxHelper(result(board, branch), False)
            if value > bestScore:
                bestScore = value
           
        return bestScore

    # O's turn, minimize score
    else:
        bestScore = math.inf 
        # find the lowest value and return
        for branch in actions(board):
            value = minimaxHelper(result(board, branch), True)
            if value < bestScore:
                bestScore = value 
        return bestScore
    
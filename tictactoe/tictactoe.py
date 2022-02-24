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
    empty_state = False
    num_X = 0
    num_O = 0

    #Iterating through each element in board
    for row in board:
        for cell in row:

            #Flag to recognize an initial state
            empty_state = (type(cell)==None)

            #Keeping track of number of Xs and Os played
            if cell=="X":
                num_X +=1
            elif cell=="O":
                num_O +=1

    #If board is in initial state
    if empty_state:
        return "X"

    #Turn of player O
    elif num_X > num_O:
        return "O"

    #Turn of player X
    elif num_X==num_O:
        return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    i = 0 
    j = 0
    s = set()

    for row in board:
        for cell in row:
            if type(cell)==None:
                s.add((i, j))
            j +=1
        i +=1
    return s


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


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    action_list = []
    val_list = []
    if player(board)=="X":
        for action in actions(board):
            val = min_value(result(board, action))
            action_list.append(action)
            val_list.append(val)
        opt_action = action_list[val_list.index(max(val_list))]

    else:
        for action in actions(board):
            val = max_value(result(board, action))
            action_list.append(action)
            val_list.append(val)
        opt_action = action_list[val_list.index(min(val_list))]
    
    return opt_action

def max_value(board):
    v = float('-inf')
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    v = float('inf')
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

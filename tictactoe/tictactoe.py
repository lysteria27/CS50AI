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
        return X

    #Turn of player O
    elif num_X > num_O:
        return O

    #Turn of player X
    elif num_X==num_O:
        return X


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


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

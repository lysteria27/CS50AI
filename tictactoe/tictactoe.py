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
    empty_state = False
    num_X = 0
    num_O = 0

    #Iterating through each element in board
    for row in board:
        for cell in row:

            #Flag to recognize an initial state
            empty_state = cell is None

            #Keeping track of number of Xs and Os played
            if cell=="X":
                num_X +=1
            elif cell=="O":
                num_O +=1

    #If board is in initial state
    if empty_state and num_X==0 and num_O==0:
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
    s = []

    for row in board:
        for cell in row:
            if cell is None:
                s.append((i, j))
            j +=1
        i +=1
        j = 0
    return s


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copy_board = copy.deepcopy(board)
    i = action[0]
    j = action[1]
    if copy_board[i][j] is EMPTY:
        copy_board[i][j] = player(copy_board)
        return copy_board
    else:
        raise Exception("Invalid action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    counter = 1

    #Checking for a winner horizontally
    for i in range(3):
        ele = board[i][0]
        for j in range(1, 3):
            if ele != board[i][j]:
                break
            else:
                counter +=1
        if counter==3:
            return ele
        counter = 1

    counter = 1
    
    #Checking for a winner vertically
    for i in range(3):
        ele = board[0][i]
        for j in range(1, 3):
            if ele != board[j][i]:
                break
            else:
                counter +=1
        if counter==3:
            return ele
        counter = 1

    #Checking for a winner on the left diagonal
    ele = board[0][0]
    if ele==board[1][1]:
        if ele==board[2][2]:
            return ele
    
    ele = board[0][2]
    if ele==board[1][1]:
        if ele==board[2][0]:
            return ele
    
    #If the neither of the conditions are satisfied
    #We have a tie
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    flag = False
    for row in board:
        for cell in row:

            #If even one cell is empty
            if cell is None:
                return False
    flag = True
    return flag


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    champ = winner(board)
    if champ=="X":
        return 1
    elif champ=="O":
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    action_list = []
    val_list = []

    if terminal(board):
        return winner(board)

    #Player X's turn
    if player(board)=="X":
        for action in actions(board):

            #Utility of each immediate action
            val = min_value(result(board, action))

            action_list.append(action)
            val_list.append(val)
        
        #Finding the optimal action by choosing one of maximum utility
        opt_action = action_list[val_list.index(max(val_list))]
    
    #Player O's turn
    else:
        for action in actions(board):

            #Utility of each immediate action
            val = max_value(result(board, action))

            action_list.append(action)
            val_list.append(val)
        
        #Finding the optimal action by choosing one of minimum utility
        opt_action = action_list[val_list.index(min(val_list))]
    
    return opt_action

def max_value(board):
    v = float('-inf')
    if terminal(board):
        return utility(board)
    elif winner(board)!=None:
        return utility(board)
    for action in actions(board):
        v1 = min_value(result(board, action))
        if v1>v:
            v = v1
            if v==1:
                return v

    return v

def min_value(board):

    v = float('inf')
    if terminal(board):
        return utility(board)
    elif winner(board)!=None:
        return utility(board)
    for action in actions(board):
        v1 = max_value(result(board, action))
        if v1<v:
            v = v1
            if v==-1:
                return v

    return v

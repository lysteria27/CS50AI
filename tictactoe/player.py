from tictactoe import EMPTY, O, X, player

#Test 1: initial state
playaa = player([[EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY]])
print(playaa)

#Test 2: Player O's turn
playaa = player([[EMPTY, EMPTY, EMPTY],
                 [EMPTY, X, EMPTY],
                 [EMPTY, EMPTY, EMPTY]])
print(playaa)

#Test #: Player X's turn
playaa = player([[EMPTY, O, O],
                 [EMPTY, X, EMPTY],
                 [X, EMPTY, EMPTY]])
print(playaa)
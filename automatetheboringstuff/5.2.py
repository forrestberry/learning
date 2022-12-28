# Chess Dictionary Validator
# Write a function named isValidChessBoard() that takes a dictionary argument
# and returns True or False depending on if the board is valid.
# A valid board will have exactly one black king and exactly one white king. Each
# player can only have at most 16 pieces, at most 8 pawns, and all pieces must be
# on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'.
# The piece names begin with either a 'w' or 'b' to represent white or black,
# followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This
# function should detect when a bug has resulted in an improper chess board.

samples = {}

board = {}
for number in range(1,9):
    for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        board[letter + str(number)] = ''

def isValidChessBoard(move):
    for key in move.keys():
        if key not in board: 
            return 'Location outside of board.'

    global wkings
    global wpawns
    global wpieces
    global bkings
    global bpawns
    global bpieces
    
    for value in move.values():
        if value[0] != 'b' and value[0] != 'w':
            return 'Specify color with b or w.'
        elif value[0] == 'b':
            bpieces += 1
            if 'pawn' in value:
                bpawns += 1
            elif 'king' in value:
                bkings += 1
            elif 'knight' not in value and 'bishop' not in value and 'rook' not in value and 'queen' not in value:
                return 'Not a valid piece'
        elif value[0] == 'w':
            wpieces += 1
            if 'pawn' in value:
                wpawns += 1
            elif 'king' in value:
                wkings += 1
            elif 'knight' not in value and 'bishop' not in value and 'rook' not in value and 'queen' not in value:
                return 'Not a valid piece'

        if bpieces > 16 or wpieces > 16:
            return 'Too many pieces on the board.'
        if bpawns > 8 or wpawns > 8:
            return 'Too many pawns on the board.'
        if bkings > 1 or wkings > 1:
            return 'Too many kings on the board.'
    return 'Valid move'
            
wkings = 0
wpawns = 0
wpieces = 0
bkings = 0
bpawns = 0
bpieces = 0
            

while True:
    move = input('Make a move (location, piece)')
    move = move.split(' ')
    samples[move[0]] = move[1]
    print(isValidChessBoard(samples))


            


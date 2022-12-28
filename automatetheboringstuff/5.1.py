# Tic Tac Toe Game
from random import choice as choice

boardstatus = {
        'top_right': ' ',
        'top_mid' : ' ',
        'top_left': ' ', 
        'mid_right': ' ',
        'mid_mid': ' ',
        'mid_left': ' ',
        'bottom_right': ' ',
        'bottom_mid': ' ',
        'bottom_left': ' '
        }

def printgame():
    newline = '\n'
    print(' ' + boardstatus['top_left'] + ' | ' + boardstatus['top_mid'] +
          ' | ' + boardstatus['top_right'] + '\n' + 
          '--- --- ---\n' + 
          ' ' + boardstatus['mid_left'] + ' | ' + boardstatus['mid_mid'] +
          ' | ' + boardstatus['mid_right'] + '\n'
          '--- --- ---\n' + 
          ' ' + boardstatus['bottom_left'] + ' | ' + boardstatus['bottom_mid'] + 
          ' | ' + boardstatus['bottom_right']
          )

def newmove():
    move = input('Make your move (TL, TM, TR, ML, MM, MR, BL, BM, BR): ')
    move = move.upper()
    if move[0] == 'T':
        move = 'top_' + move[1]
    elif move[0] == 'M':
        move = 'mid_' + move[1]
    elif move[0] == 'B':
        move = 'bottom_' + move[1]
    else:
        print('I don\'t understand that move.')
        return

    if move[-1] == 'L':
        move = move[0:-1] + 'left'
    elif move[-1] == 'R':
        move = move[0:-1] + 'right'
    elif move[-1] == 'M':
        move = move[0:-1] + 'mid'
    else:
        print('I don\'t understand that move.')
        return

    if boardstatus[move] == ' ':
        boardstatus[move] = 'O'
    else:
        print('Spot taken; choose again.')
        newmove()


def cpumove():
    while True:
        move = choice(list(boardstatus.keys()))
        if boardstatus[move] == ' ':
            boardstatus[move] = 'X'
            break
    

while True:
    printgame()
    newmove()
    cpumove()

# works as far as chapter takes me

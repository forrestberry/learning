# Rock, Paper, Scissors Game
from random import randint as ri

print('Rock, Paper, Scissors!')

wins = 0
losses = 0
draws = 0

print('Welcome to Rock, Paper, Scissors!\nBest of three!\nEnter your move:'
      '(r)ock (p)aper (s)cissors or (q)uit.') 

rounds = 0

relations = {
        'rock' : 0,
        'paper' : 1,
        'scissors' : 2
        }

while True:
    turn = input()
    match turn:
        case 'r':
            turnNum = 0
        case 'paper' | 'p' | 'P':
            turn = 1
            print(turn)
        case 'scissors' | 's' | 'S':
            turn = 2
        case _:
            print(f'Sorry, I couldn\'t understand {turn!r}')
            pass
    cpu = ri(0, 2)
    difference = int(cpu) - int(turnNum)
    match difference:
        case 1:
            losses += 1
            print(f'CPU wins!\n{wins} Wins, {losses} Losses, {draws} Draws')
        case 2:
            wins += 1
            print(f'You win!\n{wins} Wins, {losses} Losses, {draws} Draws')
        case 0:
            draws += 1
            print(f'It\'s a draw!!\n{wins} Wins, {losses} Losses, {draws} Draws')
        case -1:
            wins += 1
            print(f'You win!\n{wins} Wins, {losses} Losses, {draws} Draws')
        case -2:
            losses += 1
            print(f'CPU wins!\n{wins} Wins, {losses} Losses, {draws} Draws')
    if wins == 2 or losses == 2:
        break

print(f'That\'s the game!\n{wins} Wins, {losses} Losses, {draws} Draws')
      

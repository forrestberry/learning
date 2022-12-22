# Guess the number game
from random import randint as ri

answer = ri(1,20)

guess = int(input('Pick a number between 1 and 20.\n'))
numGuesses = 1 

while guess != answer:
    if guess > answer:
        guess = int(input('Guess was too high. Guess again.\n'))
        numGuesses += 1
    else:
        guess = int(input('Guess was too low. Guess again.\n'))
        numGuesses += 1

print(f'Correct! The answer was {answer}. You got the answer in {numGuesses} '
      'guesses.')


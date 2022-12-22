# Collatz Sequence

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(number * 3 + 1)
        return number * 3 + 1

try:
    userInput = int(input('Pick a number, any number! (As long as it is a positive integer)\n'))
except:
    print('Not an integer')
    userInput=1
    

while True:
    if userInput < 1:
        print('Not a positive integer')
        break
    if userInput == 1:
        break
    else:
        userInput = collatz(userInput)

# Question 9 Write code that prints Hello if 1 is stored in spam, prints Howdy
# if 2 is stored in spam, and prints Greetings! if anything else is stored in
# spam.

from random import randint as ri

spam = ri(1,5)

match spam:
    case 1:
        print('Hello')
    case 2:
        print('Howdy')
    case _:
        print('Greetings!')

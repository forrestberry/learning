# Print a zigzag pattern of 8 asterisks that repeats until user force quits.
import sys

try:
    while True:
        spaces = 0
        for i in range(4):
            print(' '*spaces, '*****')
            spaces += 1
        for i in range(4):
            spaces += -1
            print(' '*spaces, '*****')
except KeyboardInterrupt:
    sys.exit()
        
         
        


# Write a program to find out how often a streak of six heads or a streak of
# six tails comes up in a randomly generated list of 100 coin flips. Your
# program breaks up the experiment into two parts: the first part generates a
# list of randomly selected 'heads' and 'tails' values, and the second part
# checks if there is a streak in it. Put all of this code in a loop that
# repeats the experiment 10,000 times so we can find out what percentage of the
# coin flips contains a streak of six heads or tails in a row. As a hint, the
# function call random.randint(0, 1) will return a 0 value 50% of the time and
# a 1 value the other 50% of the time.

from random import randint as ri
from statistics import mean

percent = []

for i in range(10000):
    streaks = 0
    group = []
    
   # create flips
    for x in range(100):
        x = ri(0,1)
        group.append(x)

    # check for streaks
    for flip in group[:-6]:
        if all(group[flip:flip+6]):
            streaks += 1
        else:
            pass
    singlepercent = streaks/100
    percent.append(singlepercent)    

answer = mean(percent)
print(answer)




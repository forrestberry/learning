# Table Printer
# 
# Write a function named printTable() that takes a list of lists of strings and
# displays it in a well-organized table with each column right-justified.
# Assume that all the inner lists will contain the same number of strings. For
# example, the value could look like this:
# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# get longest string
longest = 0
for line in tableData:
    string = ' '.join(line)
    if len(string) > longest:
        longest = len(string)

def printTable(list):
    for line in list:
        string =' '.join(line)
        print(string.rjust(longest))

printTable(tableData)

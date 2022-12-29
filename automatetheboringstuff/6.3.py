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
widths = [0,0,0,0]
for line in tableData:
    position = 0
    for item in line:
        width = len(item)
        if width > widths[position]:
            widths[position] = width
        position += 1

def printTable(list):
    position = 0
    for line in list:
        for item in line:
            item = item.rjust(widths[position])
            position +=1
        string =' '.join(line)
    print(string)

printTable(tableData)

'''
Say you have a list of lists where each value in the inner lists is a one-character string, like this:
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

Think of grid[x][y] as being the character at the x- and y-coordinates of a
“picture” drawn with text characters. The (0, 0) origin is in the upper-left
corner, the x-coordinates increase going right, and the y-coordinates increase
going down.  Copy the previous grid value, and write code that uses it to print
the image.
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

Hint: You will need to use a loop in a loop in order to print grid[0][0], then
grid[1][0], then grid[2][0], and so on, up to grid[8][0]. This will finish the
first row, so then print a newline. Then your program should print grid[0][1],
then grid[1][1], then grid[2][1], and so on. The last thing your program will
print is grid[8][5].  '''



grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for x in len(grid):
    # add each vertical element to a list, i.e. 00, 10, 20, ... get added to
    # list, then 01, 11, 21, etc., then convert list to string, then print
    for element in item:
        print(grid[y][x])
        y+=1
        x+=1

#Your job is to calculate the minimum total cost when moving from the upper left corner to the coordinate given. You're only allowed to move right or down.

def fill_diagonal(r, c, grid, d, size):
    while r > 0 and c < size:
        d[r][c] = int(min(d[r-1][c], d[r][c-1]) + grid[r-1][c-1])
        r -= 1
        c += 1
    return d

def min_path(grid, x, y):
    if x == 0 and y == 0: return grid[0][0]
    l = max(x,y) + 2 #size of the table depends on how far away the searched point is
    d = [[0] * l for i in range(l)]

    for i in range(l): d[i][0] = d[0][i] = float('+inf') #making bounds

    d[1][1] = grid[0][0]
  
    #filling diagonals from the most left to the most right:
    for row in range(2, l-1): d = fill_diagonal(row, 1, grid, d, l)
    for col in range(1, l): d = fill_diagonal(l-1, col, grid, d, l)
    return d[y+1][x+1]

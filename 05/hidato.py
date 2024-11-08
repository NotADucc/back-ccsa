def eerste(grid) :
    for i in range(len(grid)) :
        for j in range(len(grid[i])) :
            if grid[i][j] == 1 :
                return (i, j)


def opvolger(grid, rij, col) :
    val = grid[rij][col]
    min_rij = rij - 1 if rij > 0 else 0
    min_col = col - 1 if col > 0 else 0
    max_rij = rij + 1 if rij + 1 < len(grid) else rij
    max_col = col + 1 if col + 1 < len(grid[rij]) else col

    for i in range(min_rij, max_rij + 1, 1) :
        for j in range(min_col, max_col + 1, 1) :
            if (grid[i][j] == val + 1) :
                return (i, j)
    
    return (None, None)


def laatste(grid) :
    rij, col = eerste(grid)
    while True :
        n_rij, n_col = opvolger(grid, rij, col)
        if n_rij is None or n_col is None :
            return (rij, col)
        rij, col = n_rij, n_col
        
def hidato(grid) :
    r, c = laatste(grid)
    return grid[r][c] == len(grid) * len(grid[0])
    
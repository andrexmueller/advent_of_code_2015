# AoC - 2015: Day 18
# from copy import deepcopy


def eval_state(r, c, grid, part_02=False):
    R, C = len(grid), len(grid[0])
    if part_02 and (r, c) in [(0, 0), (0, C-1), (R-1, 0), (R-1, C-1)]:
        return '#'
    upon = 0 if r == 0 else grid[r-1][max(0, c-1): c-1+3].count('#')
    bellow = 0 if r == R-1 else grid[r+1][max(0, c-1): c-1+3].count('#')
    right = 0 if c == 0 else grid[r][c-1].count('#') 
    left = 0 if c == C-1 else grid[r][c+1].count('#')
    neiborson = 0
    neiborson = upon + bellow + left + right
    if grid[r][c] == '#':
        if 2 <= neiborson <= 3:
            return '#'
        else:
            return '.'
    else:
        if neiborson == 3:
            return '#'
        else:
            return '.'


def eval_grid(grid, times, part_02=False):
    if times == 0:
        return grid
    R, C = len(grid), len(grid[0])
    new_grid = [[] for r in range(R)]
    for r in range(R):
        for c in range(C):
            new_grid[r].append(eval_state(r, c, grid, part_02))
    return eval_grid(new_grid, times-1, part_02)


def solve_part_01(grid, times=100):
    grid = eval_grid(grid, times)
    total = 0
    for line in grid:
        # print(''.join(line))
        total += ''.join(line).count('#')
    print(total)


def solve_part_02(grid, times=100):
    R, C  = len(grid), len(grid[0])
    for (r, c) in [(0, 0), (0, C-1), (R-1, 0), (R-1, C-1)]:
        grid[r][c] = '#'
    
    grid = eval_grid(grid, times, part_02=True)
    total = 0
    for line in grid:
        # print(''.join(line))
        total += ''.join(line).count('#')
    print(total)




grid = [list(line) for line in open(0).read().splitlines()]


solve_part_01(grid)
solve_part_02(grid,100)
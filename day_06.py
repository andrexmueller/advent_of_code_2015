import numpy as np

def solve_part_01(data):
    grid = np.zeros((1000,1000), dtype=int)
    for line in data:
        start, end = line.split(' through ')
        comm, start = start.split(' ')[-2], start.split(' ')[-1]
        rs, cs = list(map(int, start.split(',')))
        re, ce = list(map(int, end.split(',')))
        if comm == 'on':
            grid[rs:re+1, cs:ce+1] = 1
        if comm == 'off':
            grid[rs:re+1, cs:ce+1] = 0
        if comm == 'toggle':
            grid[rs:re+1, cs:ce+1] += 1
            grid[rs:re+1, cs:ce+1] %= 2

    return np.sum(grid)

            
def solve_part_02(data):
    grid = [[0 for i in range(1000)] for j in range(1000)]
    for line in data:
        start, end = line.split(' through ')
        comm, start = start.split(' ')[-2], start.split(' ')[-1]
        rs, cs = list(map(int, start.split(',')))
        re, ce = list(map(int, end.split(',')))
        if comm == 'on':
            for i in range(rs, re+1):
                for j in range(cs, ce+1):
                    grid[i][j] += 1
        if comm == 'off':
            for i in range(rs, re+1):
                for j in range(cs, ce+1):
                    grid[i][j] = max(grid[i][j]-1, 0)
        if comm == 'toggle':
            for i in range(rs, re+1):
                for j in range(cs, ce+1):
                    grid[i][j] += 2
    return sum([sum(line) for line in grid])


if __name__ == '__main__':

    instructions = open(0).read().splitlines()

    pt1 = solve_part_01(instructions)
    print(pt1)

    pt2 = solve_part_02(instructions)
    print(pt2)

move = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}

def solve_part_01(data):
    position = (0, 0)
    visited = set([position])
    
    for direction in data:
        r, c = position
        dr, dc = move[direction]
        position = (r+dr, c+dc)
        visited.add(position)

    return len(visited)
        
        
def solve_part_02(data):
    santa = (0, 0)
    robot = (0, 0)
    visited = set([santa])

    for i, direction in enumerate(data):
        sr, sc = santa
        rr, rc = robot
        dr, dc = move[direction]
        if i % 2:
            santa = (sr+dr, sc+dc)
            visited.add(santa)
        else:
            robot = (rr+dr, rc+dc)
            visited.add(robot)
    
    return len(visited)


if __name__ == '__main__':

    data = open(0).read()

    pt1 = solve_part_01(data)    
    print(pt1)
    
    pt2 = solve_part_02(data)    
    print(pt2)
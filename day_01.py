# AoC - 2015: Day 01



def solve_part_01(data):
    going_up = data.count('(')
    going_down = data.count(')')
    return going_up - going_down


def solve_part_02(data):
    position = 0
    index = 0
    while position != -1:

        move = 1 if data[index] == '(' else -1
        position += move
        index += 1
    
    return index

if __name__ == '__main__':
    
    data = open(0).read()
    

    print(solve_part_01(data))
    print(solve_part_02(data))


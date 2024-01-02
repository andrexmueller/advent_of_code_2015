# AoC - 2015: Day 02


def solve_part_01(data):
    total = 0
    for pack in data:
        lenght, width, height = sorted(list(map(int, pack.split('x'))))
        total += 2 * (lenght * width + width * height + height * lenght) + lenght * width

    return total


def solve_part_02(data):
    # shortest distance around sides or smallest perímeter arount anu face
    total = 0
    for pack in data:
        lenght, width, height = sorted(list(map(int, pack.split('x'))))
        total += 2 * (lenght + width) + lenght * width * height

    return total


if __name__ == '__main__':

    data = open(0).read().splitlines()
    
    pt1 = solve_part_01(data)
    print(pt1)
    
    pt2 = solve_part_02(data)
    print(pt2)

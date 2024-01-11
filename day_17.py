# AoC - 2015: Day 17

from collections import Counter

capacities = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]
V = 150

def solve_part_01(capacities: list, volume: int) -> None:
    volumes = list(range(volume + 1))
    capacities = [0] + sorted(capacities)
    dt = [[0 for _ in range(len(volumes))] for _ in range(len(capacities))]

    for i in range(1, len(capacities)):
        for j in range(1, len(volumes)):
            actual_capacity = 1 if capacities[i] == volumes[j] else 0
            prev = j - capacities[i]
            prev_sols = 0 if prev < 0 else dt[i-1][prev]
            same_vol = dt[i-1][j]
            dt[i][j] = actual_capacity + prev_sols + same_vol
    # for line in dt:
    #     print(line)
    print(dt[-1][-1])


def solve_part_02(capacities: list, volume: int) -> None:
    volumes = list(range(volume + 1))
    capacities = [0] + sorted(capacities)
    #dt = [[0 for _ in range(len(volumes))] for _ in range(len(capacities))]
    combos = {(r,c): [] for r in range(len(capacities)) for c in range(len(volumes))}
    C, V = len(capacities), len(volumes)
    for i in range(1, C):
        for j in range(1, V):
            prev = max(0, j - capacities[i])            
            if capacities[i] == volumes[j]:
                combos[(i, j)].append((capacities[i],))
            for c in combos[(i-1, prev)]:
                combos[(i, j)].append(c+(capacities[i],)) 
            for c in combos[(i-1, j)]:
                combos[(i, j)].append(c) 

    counter = Counter([len(c) for c in combos[(C-1, V-1)]])    
    print(counter[min(counter.keys())])


if __name__ == '__main__':

    solve_part_01(capacities, V)
    solve_part_02(capacities, V)

# AoC - 2015: Day 13
from itertools import permutations


def solve_part_01(data):
    persons = {}

    for line in data:
        p1, _, sign, hap, *p2 = line.split(' ')
        sign = 1 if sign == 'gain' else -1
        hap = int(hap)
        p2 = p2[-1][:-1]
        if p1 not in persons:
            persons[p1] = {}
        persons[p1][p2] = sign * hap

    total = 0
    for permut in permutations(persons):
        points = sum([persons[permut[i]][permut[i-1]] + persons[permut[i]][permut[(i+1)%len(permut)]] for i in range(len(permut))])
        total = max(total, points)

    print(total)


def solve_part_02(data):
    persons = {}

    for line in data:
        p1, _, sign, hap, *p2 = line.split(' ')
        sign = 1 if sign == 'gain' else -1
        hap = int(hap)
        p2 = p2[-1][:-1]
        if p1 not in persons:
            persons[p1] = {}
        persons[p1][p2] = sign * hap
    
    myself = {person: 0 for person in persons.keys()}
    for k in persons:
        persons[k]['myself'] = 0
    persons['myself'] = myself

    total = 0
    for permut in permutations(persons):
        points = sum([persons[permut[i]][permut[i-1]] + persons[permut[i]][permut[(i+1)%len(permut)]] for i in range(len(permut))])
        total = max(total, points)

    print(total)



if __name__ == '__main__':
    
    data = open(0).read().splitlines()

    solve_part_01(data)

    solve_part_02(data)
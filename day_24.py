# --- Day 24: It Hangs in the Balance ---

from itertools import combinations
from functools import reduce


lista = [1,2,3,5,7,13,17,19,23,29,31,37,41,43,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113]

"""
Despite the massive search space for this problem, we can use brute force to find the
combinations that solve the puzzle once we just need to look into those ones with the
minimum lenght, pruning enormously the search space if we sort the list in inverse order.
"""


def brute_force(lon: list, tgt: int):
    sols = []
    minum_lenght = len(lon)
    for n in range(1, len(lon)+1):
        for c in combinations(lon, n):
            if sum(c) == tgt:
                if len(c) <= minum_lenght:
                    minum_lenght = len(c)
                    sols.append(c)
                else:
                    return sols
                
def solve_part_1():
    sols = brute_force(lista, sum(lista)//3)                
    minum_qe = float('inf')
    solution = None
    for sol in sols:
        qe = reduce(lambda x, y: x * y, sol)
        if qe < minum_qe:
            solution = sol
            minum_qe = qe
    print(solution, minum_qe)


def solve_part_2():
    sols = brute_force(lista, sum(lista)//4)                
    minum_qe = float('inf')
    solution = None
    for sol in sols:
        qe = reduce(lambda x, y: x * y, sol)
        if qe < minum_qe:
            solution = sol
            minum_qe = qe
    print(solution, minum_qe)


if __name__ == '__main__':
    solve_part_1()
    solve_part_2()

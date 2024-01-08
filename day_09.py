# AoC - 2015: Day 09

from itertools import permutations


def get_data():
    
    graph = {}
    data = open(0).read().splitlines()
    for line in data:
        vw, d = line.split(' = ')
        d = int(d)
        v, w = vw.split(' to ')
        if v not in graph:
            graph[v] = {}
        if w not in graph:
            graph[w] = {}
        graph[v][w] = d
        graph[w][v] = d
    return graph


def solve_part_01(graph):
    # brute force
    distance = float('inf')
    for permutation in permutations(graph.keys()):
        distance = min(distance, sum([graph[permutation[i]][permutation[i-1]] for i in range(1,len(permutation))]))
        # print(permutation, distance)
    print(distance)

def solve_part_02(graph):
    # brute force
    distance = -float('inf')
    for permutation in permutations(graph.keys()):
        distance = max(distance, sum([graph[permutation[i]][permutation[i-1]] for i in range(1,len(permutation))]))
        # print(permutation, distance)
    print(distance)


if __name__ == '__main__':

    graph = get_data()
    solve_part_01(graph)
    solve_part_02(graph)

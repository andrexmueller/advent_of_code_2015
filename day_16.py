# AoC - 2015: Day 16

import re



def solve_part_01(data):
    
    target = [
        "children: 3",
        "cats: 7",
        "samoyeds: 2",
        "pomeranians: 3",
        "akitas: 0",
        "vizslas: 0",
        "goldfish: 5",
        "trees: 3",
        "cars: 2",
        "perfumes: 1"
    ]
    for aunt_number, line in enumerate(data):
        _, infos = re.split(r'Sue \d+: ', line)
        infos = infos.split(', ')
        if all([info in target for info in infos]):
            print(aunt_number+1)
            return


def solve_part_02(data):
    
    target = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    aunts = []
    for line in data:

        _, infos = re.split(r'Sue \d+: ', line)
        infos = infos.split(', ')
        infos = {info.split(': ')[0]: int(info.split(': ')[1]) for info in infos}
        aunts.append(infos)

    for n, aunt in enumerate(aunts):
        assessesment = True
        for k, v in aunt.items():
            if k in ['cats', 'trees']:
                if v <=target[k]:
                    assessesment = False
            elif k in ['pomeranians', 'goldfish']:
                if v>=target[k]:
                    assessesment = False
            else:
                if v != target[k]:
                    assessesment = False
        if assessesment:
            print(n+1)

if __name__ == '__main__':


    data = open(0).read().splitlines()
    solve_part_01(data)
    solve_part_02(data)

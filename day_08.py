# AoC - 2015: Day 08

import re

def solve_part_01(data):
    scapes = [r'\\x[0-9a-f]{2}', r'\\"', r"\\{2}"]
    len_literals = 0
    len_memory = 0
    for line in data:
        len_literals += len(line)
        string = line
        for scape in scapes:
            string = re.sub(scape, '.', string)
        len_memory += len(string)  - 2
        # print(line, len(line), string, len(string)-2)
    print(len_literals - len_memory)


def solve_part_02(data):
    len_string = 0
    new_len = 0
    for line in data:
        nl = len(line) + 2
        len_string += len(line)
        nl += line.count('\"')
        nl += line.count('\\')
        new_len += nl
        # print(line, len_string, nl)
    print(new_len - len_string)

if __name__ == '__main__':

    data = open(0).read().splitlines()
    solve_part_01(data)
    solve_part_02(data)




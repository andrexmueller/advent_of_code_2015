# AoC - 2015: Day 12

import re
import json


def solve_part_01(data):
    return sum([int(n) for n in re.findall(r'-*\d+', data)])

def solve_part_02(data):
    obj = json.loads(data)
    
    def recursive_sum(obj):
        total = 0
        if type(obj) == int:
            return obj
        if type(obj) == list:
            for v in obj:
                total += recursive_sum(v)
        if type(obj) == dict:
            if "red" in obj.values():
                return 0
            for v in obj.values():
                total += recursive_sum(v)
        return total
    
    return recursive_sum(obj)    

data = open(0).read()

print(solve_part_01(data))
print(solve_part_02(data))
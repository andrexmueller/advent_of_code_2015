import re

def solve_part_01(data):
    total = 0
    for string in data:
        vowels = 1 if len(re.findall('[aeiou]', string)) >= 3 else 0
        double_letters = 1 if re.search(r'(.)\1+', string) else 0
        naughty = 0 if re.search(r'(ab)|(cd)|(pq)|(xy)', string) else 1
        total += vowels * double_letters * naughty
    return total


def solve_part_02(data):
    total = 0
    for string in data:
        pair = 0
        repeats = 0
        for i in range(len(string)-2):
            if string[i:i+2] in string[i+2:]:
                pair = 1
                break
        for i in range(len(string)-2):
            if string[i] == string[i+2]:
                repeats = 1
                break
        total += pair * repeats
    return total


if __name__ == '__main__':

    data = open(0).read().splitlines()
    
    pt1  = solve_part_01(data)
    print(pt1)
    pt2  = solve_part_02(data)
    print(pt2)
# AoC - 2015: Day 11
import re


def checke_rule_01(string):
    counter = 1
    i = 1
    while i < len(string):
        if ord(string[i]) == ord(string[i-1]) + 1:
            counter += 1
        else:
            counter = 1
        if counter  == 3:
            return True
        i += 1
    return False


def checke_rule_02(string):
    return not ('i' in string or 'o' in string or 'l' in string)


def checke_rule_03(string):
    return len(re.findall(r'(.)\1+', string)) >= 2


def rotate_password(string):
    i = len(string) - 1
    char = string[i]
    while char == 'z':
        string = string[:i] + 'a' + string[i+1:]
        i -= 1
        char = string[i]
    new_char = chr(ord(string[i])+1)
    string = string[:i] + new_char + string[i+1:]
    return string


def solve_part_01(pswd):
    correct = False
    while not correct:
        pswd = rotate_password(pswd)
        correct = checke_rule_01(pswd) and checke_rule_02(pswd) and checke_rule_03(pswd)
    return pswd


def solve_part_02(pswd):
    new_pswd = solve_part_01(pswd)
    return solve_part_01(new_pswd)


print(solve_part_01('hxbxwxba'))
print(solve_part_02('hxbxwxba'))
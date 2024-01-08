# AoC - 2015: Day 10



def solve_part_01(n, x=40):
    
    for _ in range(x):
        i = 1
        c = 1
        nn = ''
        while i < len(n):
            if n[i] == n[i-1]:
                c += 1
            else:
                nn += str(c) + n[i-1]
                c = 1
            i += 1
        nn += str(c) + n[i-1]
        n = nn
    print(len(nn))

def solve_part_02(n):
    print(solve_part_01(n, 50))

if __name__ == '__main__':

    solve_part_01('3113322113')
    solve_part_02('3113322113')
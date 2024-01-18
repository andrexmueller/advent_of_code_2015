
divisors = {1: {1}, 2: {1, 2}, 3: {1, 3}}

def get_divisors(x):
    if x in divisors:
        return divisors[x]
    divs = {1, x}
    for i in range(2, int(x**.5)+1):
        if x % i == 0:
            divs.add(i)
            divs.add(x//i)
    divisors[x] = divs
    return divs


def solve_part_01(data):
    house = 0
    presents = 0
    while presents < data:
        house += 1
        presents = 10 * sum(get_divisors(house))
    print(house, presents)


def solve_part_02(data):
    house = 0
    presents = 0
    while presents < data:
        house += 1
        divs = get_divisors(house)
        presents = 11 * sum([div if div >= house / 50 else 0 for div in divs])
    print(house, presents)    
   


if __name__ == '__main__':

    from time import time
    data = 34000000
    ti = time()
    solve_part_01(data)
    tf = time()
    print('t -> ', tf - ti)
    solve_part_02(34000000)
    tf2 = time()
    print('t2 -> ', tf2-tf)

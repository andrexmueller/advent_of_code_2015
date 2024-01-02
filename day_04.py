import hashlib


def solve_part_01_02(data: str):
    c = 1
    pt1 = None
    pt2 = None
    while c <= 10_000_000:
        string = data + str(c)
        #print(string, hashlib.md5(string.encode()).hexdigest())
        hashed = hashlib.md5(string.encode()).hexdigest()
        if hashed[:5] == '00000' and hashed[6] and pt1 is None:
            pt1 = c
        if hashed[:6] == '000000':
            pt2 = c
        if pt1 and pt2:
            break
        c += 1
    
    return pt1, pt2








if __name__ == '__main__':
    
    data = 'ckczppom'

    pt1, pt2 = solve_part_01_02(data)
    print(pt1, pt2)
    

    

# --- Day 25: Let It Snow ---


# def get_ordinal_from_coords(row: int, col: int) -> int:
#     row_col0 = sum(range(row+1)) + 1
#     if col == 0:
#         return row_col0
#     return row_col0 + sum(range(row+2+col)) - sum(range(row+2))


def get_ordinal_from_coords(row: int, col: int) -> int:
    row_col0 = (row ** 2 + row) // 2 + 1
    if col == 0:
        return row_col0
    return row_col0 + ((row+1+col)**2 + (row+1+col)) // 2  - ((row+1)**2+row+1)//2


def solve_part_1(data):
    r, c = data
    code = 20151125
    factor = 252533
    modulo = 33554393
    for i in range(1, get_ordinal_from_coords(r-1, c-1)):
        code = (code * factor) % modulo
    print(code)    



if __name__ == '__main__':

    solve_part_1((2981, 3075))
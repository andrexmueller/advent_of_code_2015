# --- Day 23: Opening the Turing Lock ---

def run_program(program, a=0, b=0):

    registers = {'a': a, 'b': b}
    cursor = 0

    while True:
        if cursor < 0 or cursor >= len(program):
            break 
        inst, reg, offset = program[cursor]
        if inst == 'hlf':
            registers[reg] //= 2
            cursor += 1
        if inst == 'tpl':
            registers[reg] *= 3
            cursor += 1
        if inst == 'inc':
            registers[reg] += 1
            cursor += 1
        if inst == 'jmp':
            cursor += offset
        if inst == 'jie':
            if registers[reg] % 2 == 0:
                cursor += offset
            else:
                cursor += 1
        if inst == 'jio':
            if registers[reg] == 1:
                cursor += offset
            else:
                cursor += 1
        
        if  not 0 < cursor <= len(program):
            programm_end = True

    return registers['b']


def solve_part_1():
    print(run_program(program))


def solve_part_2():
    print(run_program(program, a=1))


if __name__ == '__main__':



    data = open(0).read().splitlines()
    program = []
    
    for line in data:
        
        inst, *reg = line.split()
        if len(reg) == 1 and inst != 'jmp':
            reg = reg[0][0]
            offset = None
        elif inst == 'jmp':
            offset = int(reg[0])
            reg = None
        else:
            reg, offset = reg[0][0], int(reg[1])
        
        program.append((inst, reg, offset))

    solve_part_1()
    solve_part_2()
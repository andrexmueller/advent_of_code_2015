import re

def solve_part_01(data):

    replacements, molecule = data.split('\n\n')
    replacements = [line.split(' => ') for line in replacements.split('\n')]

    new_molecules = set()

    for old, new in replacements:
        matches = re.finditer(old, molecule)
        for m in matches:
            s, f = m.span()
            nm = molecule[:s] + new + molecule[f:]
            new_molecules.add(nm)

    print(len(new_molecules))


def solve_patye_02(data):

    replacements, molecule = data.split('\n\n')
    replacements = [line.split(' => ') for line in replacements.split('\n')]
    replacements = {rep[1]: rep[0] for rep in replacements}
    
    counter = 0
    while molecule != 'e':
        for k, v in replacements.items():
            mt = re.search(k, molecule)
            if mt:
                s, f = mt.span()
                molecule = molecule[:s] + v + molecule[f:]
                #print(molecule)
                counter += 1
                continue
    
    print(counter)

if __name__ == '__main__':

    data = open(0).read()
    solve_part_01(data)
    solve_patye_02(data)
    
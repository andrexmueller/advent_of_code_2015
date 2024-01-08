from __future__ import annotations
import re


def set_connections(data):
    wires = {}
    conns = []
    for line in data:
        u_v, w = line.split(' -> ')
        gate = re.search(r'[A-Z]+', u_v)
        if gate:
            gate = u_v[gate.span()[0]: gate.span()[1]]
            u, v = [s.strip() for s in re.split(r'[A-Z]+', u_v)]

            if u.isdigit():
                wires[u] = int(u)
            else:
                if u not in wires.keys():
                    wires[u] = None

            if v.isdigit():
                wires[v] = int(v)
            else:
                if v not in wires.keys():
                    wires[v]: None

            if w not in wires.keys():
                wires[w] = None
            conns.append((u, gate, v, w))
        else:
            if u_v.isdigit():
                wires[w] = int(u_v)
            else:
                wires[w] = u_v    
    return wires, conns


def solve_part_01(data, wires=None, conns=None):
    
    if wires is None and conns is None:
        wires, conns = set_connections(data)
    

    while conns:
        u, g, v, w = conns.pop()
        u_val = wires[u]
        v_val = wires[v]

        while type(u_val) == str:
            u_val = wires[u_val]
        while type(v_val) == str:
            v_val = wires[v_val]    
        if g == 'NOT' and v_val is not None:
            wires[w] = 2**16 + ~wires[v]
            continue
        
        if u_val is not None and v_val is not None:
            if g == 'AND':
                wires[w] = u_val & v_val
            if g == 'OR':
                wires[w] = u_val | v_val
            if g == 'LSHIFT':
                wires[w] = u_val << v_val
            if g == 'RSHIFT':
                wires[w] = u_val >> v_val
            continue
        conns = [(u, g, v, w)] + conns

    ans = wires['a']
    while type(ans) is not int:
        ans = wires[ans]
    return ans


def solve_part_02(data):
    wires, conns = set_connections(data)
    wires['b'] = 3176
    ans = solve_part_01(data, wires, conns)
    return ans



if __name__ == '__main__':

    data = open(0).read().splitlines()

    tp1 = solve_part_01(data)
    print(tp1)
    
    tp2 = solve_part_02(data)
    print(tp2)


from __future__ import annotations
from itertools import product 

weapons = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0)
]

armors = [
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5)
]

rings = [    
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3)
]



class Player:
    def __init__(self, name: str, hp: int, damage: int, armor: int) -> None:
        self._orignal_stats = (hp, damage, armor)
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.alive = True
        self.equipment_cost = 0

    def attack(self, p2: Player) -> None:
        dm = max(1, self.damage - p2.armor)
        p2.hp -= dm
        if p2.hp <= 0:
            p2.alive = False

    def equip(self, weapon: int, armor: int, ring1: int, ring2: int) -> None:
        # -1: not equipped. from 0 ~ n: equip item
        if weapon >= 0:
            self.equipment_cost += weapons[weapon][0]
            self.damage += weapons[weapon][1]
        
        if armor >= 0:
            self.equipment_cost += armors[armor][0]
            self.armor += armors[armor][2]
        
        if ring1 >= 0:
            self.equipment_cost += rings[ring1][0]
            self.damage += rings[ring1][1]
            self.armor += rings[ring1][2]
        
        if ring2 >= 0 and ring2 != ring1:
            self.equipment_cost += rings[ring2][0]
            self.damage += rings[ring2][1]
            self.armor += rings[ring2][2]
            

    def reset(self) -> None:
        self.hp = self._orignal_stats[0]
        self.damage = self._orignal_stats[1]
        self.armor = self._orignal_stats[2]
        self.equipment_cost = 0
        self.alive = True


    def __str__(self):
        return f"{self.name} with {self.hp} HP"

def run_battle(p1: Player, p2: Player) -> Player:
    turn = 0
    while True:
        #print(p1.hp, p2.hp)
        if turn % 2 == 0:
            p1.attack(p2)
        else:
            p2.attack(p1)
        turn += 1
        if not p1.alive:
            return p2
        if not p2.alive:
            return p1


def solve_part_01(**args):

    p1 = Player('p1', 100, 0, 0)
    boss = Player('boss', args['hp'], args['damage'], args['armor'])

    least_cost = float('inf')
    #outfit = None

    #score = 0
    #rounds = 0

    for p in product(
        list(range(len(weapons))), 
        list(range(-1, len(armors))),
        list(range(-1, len(rings))),
        list(range(-1, len(rings)))
        ):
        #rounds += 1
        p1.equip(*p)
        winner = run_battle(p1, boss)
        #score = score + 1 if winner == p1 else score - 1
        if winner == p1 and winner.equipment_cost < least_cost:
            least_cost = winner.equipment_cost
            #outfit = p
        p1.reset()
        boss.reset()

    # print(least_cost, outfit, score, rounds)
    print("Least cost = ", least_cost)



def solve_part_02(**args):
    p1 = Player('p1', 100, 0, 0)
    boss = Player('boss', args['hp'], args['damage'], args['armor'])

    max_cost = 0
    #outfit = None

    for p in product(
        list(range(len(weapons))), 
        list(range(-1, len(armors))),
        list(range(-1, len(rings))),
        list(range(-1, len(rings)))
        ):
        p1.equip(*p)
        if run_battle(p1, boss) == boss and p1.equipment_cost > max_cost:
            max_cost = p1.equipment_cost
            outfit = p
        p1.reset()
        boss.reset()

    # print(least_cost, outfit)
    print("Max cost = ", max_cost)



if __name__ == '__main__':

    solve_part_01(hp=109, damage=8, armor=2)
    solve_part_02(hp=109, damage=8, armor=2)

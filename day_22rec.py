from collections import namedtuple
            
min_mana_usage = float('inf')

def run_turn(
    mana_usage: int,
    wiz_hp: int,
    wiz_mana: int,
    bos_hp: int,
    bos_dam: int,
    shields: int,
    poisons: int,
    recharges: int,
    turn: int,
    hard: bool
) -> int:
    
    global min_mana_usage
    
    if turn == 0 and hard:
        wiz_hp -= 1
        if wiz_hp <= 0:
            return
        
    
    if mana_usage >= min_mana_usage:
        return
    
    wiz_armor = 0

    # evaluate active spells
    if shields > 0:
        wiz_armor += 7
        shields -= 1
    if poisons > 0:
        bos_hp -= 3
        poisons -= 1
    if recharges > 0:
        wiz_mana += 101
        recharges -= 1


    #checks if boss is dead
    if bos_hp <= 0:
        min_mana_usage = min(min_mana_usage, mana_usage)
        return

    # wizard's turn
    if turn == 0:

        # casts missile
        if wiz_mana >= 53:
            if bos_hp - 4 <= 0: # boss dies
                min_mana_usage = min(min_mana_usage, mana_usage + 53)
            else:
                run_turn(mana_usage+53, wiz_hp, wiz_mana-53, bos_hp-4, bos_dam, 
                         shields, poisons, recharges, 1, hard)

        # casts drain
        if wiz_mana >= 73:
            if bos_hp - 2 <= 0: # boss dies
                min_mana_usage = min(min_mana_usage, mana_usage + 73)
            else:
                run_turn(mana_usage+73, wiz_hp+2, wiz_mana-73, bos_hp-2, bos_dam, 
                         shields, poisons, recharges, 1, hard)

        # casts shield
        if shields == 0 and wiz_mana >= 113:
            run_turn(mana_usage+113, wiz_hp, wiz_mana-113, bos_hp, bos_dam, 
                     6, poisons, recharges, 1, hard)

        # casts poison
        if poisons == 0 and wiz_mana >= 173:
            run_turn(mana_usage+173, wiz_hp, wiz_mana-173, bos_hp, bos_dam,
                     shields, 6, recharges, 1, hard)
        
        # casts recharge
        if recharges == 0 and wiz_mana >= 229:
            run_turn(mana_usage+229, wiz_hp, wiz_mana-229, bos_hp, bos_dam,
                     shields, poisons, 5, 1, hard)


    # boss' turn
    if turn == 1:

        wiz_hp -= max(bos_dam - wiz_armor, 1)
        if wiz_hp > 0:
            run_turn(mana_usage, wiz_hp, wiz_mana, bos_hp, bos_dam,
                     shields, poisons, recharges, 0, hard)
    

def solve_part_1():
    global min_mana_usage
    min_mana_usage = float('inf')
    run_turn(0, 50, 500, 55, 8, 0, 0, 0, 0, False)
    print(min_mana_usage)


def solve_part_2():
    global min_mana_usage
    min_mana_usage = float('inf')
    run_turn(0, 50, 500, 55, 8, 0, 0, 0, 0, True)
    print(min_mana_usage)



if __name__ == '__main__':

    solve_part_1()
    solve_part_2()

    
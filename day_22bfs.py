from collections import namedtuple
from queue import PriorityQueue


GameState = namedtuple('GameState', [
    'mana_usage',
    'wiz_hp',
    'wiz_mana',
    'bos_hp', 
    'bos_damage',
    'shield',
    'poison',
    'recharge',
    'turn'
])


pq = PriorityQueue()

start = GameState(0, 50, 500, 55, 8, 0, 0, 0, 0)
pq.put(start)


min_mana_usage = float('inf')

while not pq.empty():
    mu, wh, wm, bh, bd, st, pt, rt, t = pq.get()
    #print(mu, wh, wm, bh, bd, st, pt, rt, t)
    
    if mu >= min_mana_usage:
        continue
    wiz_armor = 0
    

    # # hard mode (1309 wrong ans - 1196 wa)
    if t == 0 :
        wh -= 1
        if wh <= 0:
            continue



    # evaluate active spells
    if st > 0:
        wiz_armor += 7
        st -= 1
    if pt > 0:
        bh -= 3
        pt -= 1
    if rt > 0:
        wm += 101
        rt -= 1
    
    # wizard turn - try all possible spells
    if t == 0:


        # # hard mode (1309 wrong ans - 1196 wa)
        # wh -= 1
        # if wh <= 0:
        #     continue

        # cast missile
        if wm >= 53:
            if bh - 4 <= 0: # boss dies:
                min_mana_usage = min(min_mana_usage, mu+53)
                #print('wizard wins')
            else:
                new_game_state = GameState(mu+53, wh, wm-53, bh-4, bd, st, pt, rt, 1)
                pq.put(new_game_state)
        
        # cast drain
        if wm >= 73:
            if bh - 2 <= 0: # boss dies:
                min_mana_usage = min(min_mana_usage, mu+73)
                #print('wizard wins')
            else:
                new_game_state = GameState(mu+73, wh+2, wm-73, bh-2, bd, st, pt, rt, 1)
                pq.put(new_game_state)
        
        # cast shield
        if st == 0 and wm >= 113:
            new_game_state = GameState(mu+113, wh, wm-113, bh, bd, 6, pt, rt, 1)
            pq.put(new_game_state)
        
        # cast poison
        if pt == 0 and wm >= 173:
            new_game_state = GameState(mu+173, wh, wm-173, bh, bd, st, 6, rt, 1)
            pq.put(new_game_state)

        # cast recharge
        if rt == 0 and wm >= 229:
            new_game_state = GameState(mu+229, wh, wm-229, bh, bd, st, pt, 5, 1)
            pq.put(new_game_state)
        
    # boss turn
    if t == 1:
        # checks if boss is dead
        if bh <= 0:
            min_mana_usage = min(min_mana_usage, mu)
            continue
        
        wh -= max(bd - wiz_armor, 1)
        if wh > 0: # wizard still alive
            new_game_state = GameState(mu, wh, wm, bh, bd, st, pt, rt, 0)
            pq.put(new_game_state)



# ex1=226 ex2=641

print(min_mana_usage)
    











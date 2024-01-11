# AoC - 2015: Day 14
from dataclasses import dataclass

@dataclass
class Reindeer:
    r: str
    v: int
    t: int
    d: int
    points: int = 0
    position: int = 0

    def distance(self, time: int):
        if time < self.t:
            self.position = self.v * time
            return self.position
        if self.t + self.d > time > self.t:
            self.position = self.t * self.v 
            return self.position
        t0, t1 = divmod(time, self.t+self.d)
        self.position = t0 * self.t * self.v + min(t1, self.t) * self.v
        return self.position

    
def solve_part_01(data):
    total = []
    for line in data:
        r, _, _, v, _, _, t, *d = line.split(' ')
        v = int(v)
        t = int(t)
        d = int(d[-2])
        rd = Reindeer(r, v, t, d)
        total.append(rd.distance(2503))
    print(max(total))


def solve_part_02(data):
    rds = []
    for line in data:
        r, _, _, v, _, _, t, *d = line.split(' ')
        v = int(v)
        t = int(t)
        d = int(d[-2])
        rd = Reindeer(r, v, t, d)
        rds.append(rd)
    
    for t in range(1, 2504):
        positions = [rd.distance(t) for rd in rds]
        first = max(positions)
        for rd in rds:
            if rd.position == first:
                rd.points += 1

    print(max([rd.points for rd in rds]))

if __name__ == '__main__':

    data = open(0).read().splitlines()
    solve_part_01(data)
    solve_part_02(data)
# AoC - 2015: Day 15
from dataclasses import dataclass
from typing import List

@dataclass
class Ingredient:
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    def score(self, qt: int) -> int:
        return qt * (self.capacity + self.durability + self.flavor + self.texture)

ingredients = {
    'sprinkles': Ingredient(5, -1, 0, 0, 5),
    'peanut_butter': Ingredient(-1, 3, 0, 0, 1),
    'frosting': Ingredient(0, -1, 4, 0, 6),
    'sugar': Ingredient(-1, 0, 0, 2, 8)
}

def eval_score(ingredients: List[Ingredient], quants: List[int]) -> int:
    capacity = max(0, sum([ing.capacity * qt for ing, qt in zip(ingredients, quants)]))
    durability = max(0, sum([ing.durability * qt for ing, qt in zip(ingredients, quants)]))
    flavor = max(0, sum([ing.flavor * qt for ing, qt in zip(ingredients, quants)]))
    texture = max(0, sum([ing.texture * qt for ing, qt in zip(ingredients, quants)]))
    return capacity * durability * flavor * texture

def eval_calories(ingredients: List[Ingredient], quants: List[int]) -> int:
    return sum([ing.calories * qt for ing, qt in zip(ingredients, quants)])


def solve_part_01(n):
    # brute force
    ings = list(ingredients.values())
    best_score = 0
    best_combo = None
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                for l in range(n+1):
                    if i + j + k + l == n:
                        score = eval_score(ings, [i, j, k, l])
                        if score > best_score:
                            best_score = score
                            best_combo = (i, j, k, l)
    print(best_score, best_combo)

def solve_part_02(n):
    ings = list(ingredients.values())
    best_score = 0
    best_combo = None
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                for l in range(n+1):
                    if i + j + k + l == n and eval_calories(ings, (i, j, k, l)) == 500:
                        score = eval_score(ings, [i, j, k, l])
                        if score > best_score:
                            best_score = score
                            best_combo = (i, j, k, l)
    print(best_score, best_combo)


#solve_part_01(100)
solve_part_02(100)

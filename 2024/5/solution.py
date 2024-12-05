# https://adventofcode.com/2024/day/5

from pathlib import Path
from collections import defaultdict

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    rules_str, updates_str = [x.split() for x in f.read().split("\n\n")]


solution_1 = 0
solution_2 = 0

rules = {tuple(map(int, s.split("|"))) for s in rules_str}
rules_dict = defaultdict(list)
for a, b in rules:
    rules_dict[a].append(b)

updates = [list(map(int, s.split(","))) for s in updates_str]


def is_valid_update(update: list[int]):
    for i in range(len(update) - 1):
        for j in range(i, len(update)):
            if (update[j], update[i]) in rules:
                return False
    return True


def order_update(update: list[int]):
    new_update = []

    for number in update:
        index = len(new_update)
        if number in rules_dict:
            while any(n in new_update[:index] for n in rules_dict[number]):
                index -= 1
        new_update.insert(index, number)
    return new_update


for update in updates:
    if is_valid_update(update):
        solution_1 += update[int(len(update) / 2)]
    else:
        fixed = order_update(update)
        solution_2 += fixed[int(len(fixed) / 2)]


print("Solution 1 - ", solution_1)
print("Solution 2 - ", solution_2)

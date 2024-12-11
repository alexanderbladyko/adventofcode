# https://adventofcode.com/2024/day/11

from pathlib import Path
from functools import lru_cache
from collections import Counter

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    numbers = [int(v) for v in f.read().split()]

solution_1 = 0
solution_2 = 0

BLINKS = 25
BLINKS_2 = 75


@lru_cache(maxsize=None)
def numbers_after_blink(number):
    if number == 0:
        return [1]
    size = len(str(number))
    if size % 2 == 0:
        divider = 10 ** (size / 2)
        return [int(number / divider), int(number % divider)]
    return [number * 2024]


def blink(counter):
    new_counter = Counter()
    for stone, count in counter.items():
        for num in numbers_after_blink(stone):
            new_counter[num] += count
    return new_counter


counter = Counter(numbers)
for i in range(BLINKS_2):
    print(i)
    if i == BLINKS:
        solution_1 = sum(v for v in counter.values())
    counter = blink(counter)

print(f"Solution 1 - {solution_1}")

print(f"Solution 2 - {sum(v for v in counter.values())}")

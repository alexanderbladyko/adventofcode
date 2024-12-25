# https://adventofcode.com/2024/day/25

from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    blocks = f.read().split("\n\n")

locks = []
keys = []

N = len(blocks[0].split("\n"))
M = len(blocks[0].split("\n")[0])


for block in blocks:
    if block[0] == "#":
        lock = [0] * M
        for row in block.split("\n"):
            for i, char in enumerate(row):
                if char == "#":
                    lock[i] += 1
        locks.append(lock)
    else:
        key = [0] * M
        for row in block.split("\n"):
            for i, char in enumerate(row):
                if char == "#":
                    key[i] += 1
        keys.append(key)


solution_1 = 0
for lock in locks:
    for key in keys:
        fits = True
        for i in range(M):
            if key[i] + lock[i] > N:
                fits = False
        if fits:
            solution_1 += 1

print("Solution 1 - ", solution_1)

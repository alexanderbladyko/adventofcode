# https://adventofcode.com/2024/day/8

from pathlib import Path
from collections import defaultdict
from itertools import combinations

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.read().split("\n")

N = len(lines)
M = len(lines[0])


anthenas = defaultdict(list)

for i, line in enumerate(lines):
    for j, char in enumerate(line.strip()):
        if char != ".":
            anthenas[char].append((i, j))

antinodes = set()
line_antinodes = set()


def add_antinode(a: tuple[int, int], b: tuple[int, int]):
    dx, dy = b[0] - a[0], b[1] - a[1]
    x, y = b[0] + dx, b[1] + dy
    if 0 <= x < N and 0 <= y < M:
        antinodes.add((x, y))


def trace_antinodes(a: tuple[int, int], b: tuple[int, int]):
    dx, dy = b[0] - a[0], b[1] - a[1]
    x, y = b[0] + dx, b[1] + dy
    while 0 <= x < N and 0 <= y < M:
        line_antinodes.add((x, y))
        x += dx
        y += dy


for positions in anthenas.values():
    line_antinodes.update(positions)
    for a, b in combinations(positions, r=2):
        add_antinode(a, b)
        add_antinode(b, a)

        trace_antinodes(a, b)
        trace_antinodes(b, a)


# # Used to debug
# p = Path(__file__).with_name("output.txt")
# with p.open("w") as f:
#     for i, line in enumerate(lines):
#         f.write(
#             "".join(
#                 char if (i, j) not in antinodes else "#" for j, char in enumerate(line)
#             )
#         )

print(f"Solution 1 - {len(antinodes)}")
print(f"Solution 2 - {len(line_antinodes)}")

# https://adventofcode.com/2024/day/4

from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.read().splitlines()

N = len(lines)
M = len(lines[0].strip())

solution_1 = 0
solution_2 = 0

DIRECTIONS = [
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
]

PATTERN = [
    ((-1, -1), (0, 0), (1, 1)),
    ((1, 1), (0, 0), (-1, -1)),
    ((1, -1), (0, 0), (-1, 1)),
    ((-1, 1), (0, 0), (1, -1)),
]


def check_xmas(i, j, direction, word="XMAS"):
    dx, dy = direction
    x, y = i, j
    for char in word:
        if not (0 <= x < N and 0 <= y < M) or lines[x][y] != char:
            return False
        x += dx
        y += dy
    return True


def check_mas(i, j, pattern):
    for index, dir in enumerate(pattern):
        x = i + dir[0]
        y = j + dir[1]
        if not (0 <= x < N and 0 <= y < M) or lines[x][y] != "MAS"[index]:
            return False
    return True


def check_x_mas(i, j):
    count = 0
    for pattern in PATTERN:
        if check_mas(i, j, pattern):
            count += 1
    return count == 2


for i, line in enumerate(lines):
    for j, char in enumerate(line):
        for direction in DIRECTIONS:
            if check_xmas(i, j, direction):
                solution_1 += 1
        if check_x_mas(i, j):
            solution_2 += 1


print("Solution 1 - ", solution_1)
print("Solution 2 - ", solution_2)

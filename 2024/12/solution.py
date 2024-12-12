# https://adventofcode.com/2024/day/12

from pathlib import Path
from collections import deque

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.read().split("\n")

N = len(lines)
M = len(lines[0])


DIRECTIONS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

CORNERS = [
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1),
]


def get_area(sx, sy):
    plant = lines[sx][sy]
    visited = set([(sx, sy)])
    shape = set([(sx, sy)])
    perimeter = 0
    queue = deque([(sx, sy)])
    while queue:
        x, y = queue.pop()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if lines[nx][ny] == plant and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    shape.add((nx, ny))
                    queue.append((nx, ny))
                elif lines[nx][ny] != plant:
                    perimeter += 1
            else:
                perimeter += 1
    return shape, perimeter


def get_sides(shape):
    sides = 0

    for x, y in shape:
        for dx, dy in CORNERS:
            if (x + dx, y) not in shape and (x, y + dy) not in shape:
                sides += 1

            if (
                (x, y + dy) in shape
                and (x + dx, y) in shape
                and (x + dx, y + dy) not in shape
            ):
                sides += 1

    return sides


solution_1 = 0
solution_2 = 0
visited = set()
for i in range(N):
    for j in range(M):
        if (i, j) not in visited:
            shape, perimeter = get_area(i, j)
            visited = visited.union(shape)
            solution_1 += len(shape) * perimeter
            solution_2 += len(shape) * get_sides(shape)

print("Solution 1 - ", solution_1)
print("Solution 2 - ", solution_2)

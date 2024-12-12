# https://adventofcode.com/2024/day/11

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
            if (nx, ny) in visited:
                continue
            visited.add((nx, ny))
            if 0 <= nx < N and 0 <= ny < M:
                if lines[nx][ny] == plant:
                    shape.add((nx, ny))
                    queue.append((nx, ny))
                elif lines[nx][ny] != plant:
                    perimeter += 1
            else:
                perimeter += 1
    return shape, perimeter


solution_1 = 0
visited = set()
for i in range(N):
    for j in range(M):
        if (i, j) not in visited:
            shape, perimeter = get_area(i, j)
            print(lines[i][j], shape, len(shape), perimeter)
            visited = visited.union(shape)
            solution_1 += len(shape) * perimeter

print("Solution 1 - ", solution_1)
# print("Solution 2 - ", solution_2)

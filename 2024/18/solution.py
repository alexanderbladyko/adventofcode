# https://adventofcode.com/2024/day/18

from pathlib import Path
from collections import deque
from bisect import bisect_left

N = 71
M = 71

DIRECTIONS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()
values = [tuple(map(int, line.split(","))) for line in lines]

grid = []
for i in range(M):
    grid.append([0] * N)

for x, y in values[:1024]:
    grid[y][x] = 1


def bfs(grid, start, end):
    visited = set()
    q = deque([(start, 0)])

    while q:
        (x, y), steps = q.popleft()

        if (x, y) == end:
            return steps, True

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < N
                and 0 <= ny < M
                and grid[ny][nx] == 0
                and (nx, ny) not in visited
            ):
                visited.add((nx, ny))
                q.append(((nx, ny), steps + 1))

    return -1, False


solution_1 = bfs(grid, (0, 0), (N - 1, M - 1))
print("Solution 1 - ", solution_1)


def check_grid(index):
    grid = []
    for i in range(M):
        grid.append([0] * N)

    for x, y in values[:index]:
        grid[y][x] = 1

    _, can_finish = bfs(grid, (0, 0), (N - 1, M - 1))
    return not can_finish


index = bisect_left(range(1024, len(values) + 1), True, key=check_grid) + 1023
print(f"Solution 2 - {values[index][0]},{values[index][1]}")

# https://adventofcode.com/2024/day/20

import heapq
from pathlib import Path


p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    grid = f.read().split("\n")


N = len(grid)
M = len(grid[0])

start = (0, 0)
end = (0, 0)
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == "E":
            end = (x, y)
        if char == "S":
            start = (x, y)


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
CHEAT_OPTIONS = []
for x in range(-N, N + 1):
    for y in range(-N, N + 1):
        if not (x == 0 and y == 0) and (abs(x) + abs(y) <= 20):
            CHEAT_OPTIONS.append((x, y))


print(CHEAT_OPTIONS)


def dijkstra(grid, start):
    paths = []
    for row in grid:
        paths.append([-1] * len(row))

    pq = [(0, start)]

    while pq:
        points, (x, y) = heapq.heappop(pq)

        if points > paths[y][x] and paths[y][x] != -1:
            continue

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            new_points = points + 1
            if (
                0 <= nx < N
                and 0 <= ny < M
                and grid[ny][nx] != "#"
                and (new_points < paths[ny][nx] or paths[ny][nx] == -1)
            ):
                heapq.heappush(pq, (new_points, (nx, ny)))
                paths[ny][nx] = new_points

    return paths


solution_1 = 0
paths = dijkstra(grid, start)
for x in range(N):
    for y in range(M):
        if grid[y][x] == "#":
            neighbours = []
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and paths[ny][nx] != -1:
                    neighbours.append(paths[ny][nx])
            if len(neighbours) > 1:
                if max(neighbours) - min(neighbours) - 2 >= 100:
                    solution_1 += 1

print("Solution 1 - ", solution_1)

solution_2 = 0
for x in range(N):
    for y in range(M):
        if grid[y][x] != "#":
            for dx, dy in CHEAT_OPTIONS:
                nx, ny = x + dx, y + dy
                path = abs(dx) + abs(dy)
                if (
                    0 <= nx < N
                    and 0 <= ny < M
                    and paths[ny][nx] != -1
                    and paths[ny][nx] - paths[y][x] - path >= 100
                ):
                    solution_2 += 1

print("Solution 2 - ", solution_2)

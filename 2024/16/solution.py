# https://adventofcode.com/2024/day/16

from pathlib import Path

import heapq
from collections import deque

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    grid = f.read().split("\n")

start = (0, 0)
end = (0, 0)
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == "E":
            end = (x, y)
        if char == "S":
            start = (x, y)

TURN_POINTS = 1000
MOVE_POINTS = 1

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dijkstra(grid, start, end, initial_direction=0):
    visited = dict()
    pq = [(0, (start[0], start[1], initial_direction))]

    while pq:
        points, (x, y, direction) = heapq.heappop(pq)

        if visited.get((x, y, direction), float("inf")) < points:
            continue

        dx, dy = DIRECTIONS[direction]
        if grid[y + dy][x + dx] != "#":
            new_points = points + MOVE_POINTS
            new_position = (x + dx, y + dy, direction)
            if visited.get(new_position, float("inf")) > new_points:
                visited[new_position] = new_points
                heapq.heappush(pq, (new_points, new_position))

        for new_direction in [
            (direction - 1 + len(DIRECTIONS)) % len(DIRECTIONS),
            (direction + 1) % len(DIRECTIONS),
        ]:
            new_points = points + TURN_POINTS
            new_position = (x, y, new_direction)
            if visited.get(new_position, float("inf")) > new_points:
                visited[new_position] = new_points
                heapq.heappush(pq, (new_points, new_position))

    return min(visited[(end[0], end[1], d)] for d in range(len(DIRECTIONS))), visited


def shortest_paths_tiles(grid, visited, start, end):
    tiles = set()
    queue = deque()

    end_points = min(visited[(end[0], end[1], d)] for d in range(len(DIRECTIONS)))

    for direction in range(len(DIRECTIONS)):
        position = (end[0], end[1], direction)
        if position in visited and visited[position] == end_points:
            tiles.add(end)
            queue.append(position)

    while queue:
        position = queue.popleft()
        points = visited[position]

        x, y, d = position
        dx, dy = DIRECTIONS[d]
        nx, ny = x - dx, y - dy
        if grid[ny][nx] != "#":
            new_points = points - MOVE_POINTS
            new_position = (nx, ny, d)
            if new_position in visited and visited[new_position] == new_points:
                tiles.add((nx, ny))
                queue.append(new_position)

        for new_direction in [
            (d - 1 + len(DIRECTIONS)) % len(DIRECTIONS),
            (d + 1) % len(DIRECTIONS),
        ]:
            new_position = (x, y, new_direction)
            new_points = points - TURN_POINTS
            if new_position in visited and visited[new_position] == new_points:
                tiles.add((x, y))
                queue.append(new_position)
    return tiles


def print_grid(tiles):
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            print("O" if (x, y) in tiles else char, end="")
        print()
    print()


solution_1, visited = dijkstra(grid, start, end)
print("Solution 1 - ", solution_1)

tiles = shortest_paths_tiles(grid, visited, start, end)
# print_grid(tiles)
print("Solution 2 - ", len(tiles))

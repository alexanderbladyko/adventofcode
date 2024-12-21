# https://adventofcode.com/2024/day/21

import heapq
from pathlib import Path
from functools import lru_cache


p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    codes = f.read().split("\n")


NUMERIC_KEYBOARD = (("7", "8", "9"), ("4", "5", "6"), ("1", "2", "3"), ("#", "0", "A"))
N = len(NUMERIC_KEYBOARD)
M = len(NUMERIC_KEYBOARD[0])

DIRECTIONAL_KEYBOARD = (
    ("#", "^", "A"),
    ("<", "v", ">"),
)


DIRECTIONAL_POSSIBLE_ROUTES = {
    "A": {
        "A": ["A"],
        "<": ["v<<A"],
        ">": ["vA"],
        "v": ["v<A", "<vA"],
        "^": ["<A"],
    },
    "<": {
        "A": [">>^A"],
        "<": ["A"],
        ">": [">>A"],
        "v": [">A"],
        "^": [">^A"],
    },
    "v": {
        "A": [">^A"],
        ">": [">A"],
        "<": ["<A"],
        "^": ["^A"],
        "v": ["A"],
    },
    "^": {
        "A": [">A"],
        ">": ["v>A", ">vA"],
        "v": ["vA"],
        "<": ["v<A"],
        "^": ["A"],
    },
    ">": {
        "A": ["^A"],
        "<": ["<<A"],
        "v": ["<A"],
        "^": ["<^A", "^<A"],
        ">": ["A"],
    },
}

DIRECTIONS = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, -1),
    "v": (0, 1),
}


def get_paths(grid, start, end):
    if start == end:
        return ["A"]
    sx, sy = 0, 0
    ex, ey = 0, 0
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if grid[y][x] == start:
                sx, sy = x, y
            if grid[y][x] == end:
                ex, ey = x, y

    p1 = ">" * abs(ex - sx) if ex > sx else "<" * abs(ex - sx)
    p2 = "v" * abs(ey - sy) if ey > sy else "^" * abs(ey - sy)

    paths = []
    valid = True
    x, y = sx, sy
    for symbol in p1 + p2:
        x += DIRECTIONS[symbol][0]
        y += DIRECTIONS[symbol][1]
        if grid[y][x] == "#":
            valid = False

    if valid:
        paths.append(p1 + p2 + "A")

    valid = True
    x, y = sx, sy
    for symbol in p2 + p1:
        x += DIRECTIONS[symbol][0]
        y += DIRECTIONS[symbol][1]
        if grid[y][x] == "#":
            valid = False

    if valid:
        paths.append(p2 + p1 + "A")

    return paths


def get_numeric_paths(code, index, prev_paths):
    if index == len(code) - 1:
        return prev_paths
    results = set()
    paths = get_paths(NUMERIC_KEYBOARD, code[index], code[index + 1])
    for path in paths:
        if not prev_paths:
            results.add(path)
        for prev_path in prev_paths:
            results.add(prev_path + path)

    return get_numeric_paths(code, index + 1, results)


@lru_cache(maxsize=None)
def get_possible_paths(path):
    if len(path) <= 1:
        return []
    routes = DIRECTIONAL_POSSIBLE_ROUTES[path[0]][path[1]]
    next_routes = get_possible_paths(path[1:])
    result = set()
    for route in routes:
        if not next_routes:
            result.add(route)
        for next_route in next_routes:
            result.add(route + next_route)
    return list(result)


@lru_cache(maxsize=None)  # use lru cache to cache known results to be reused
def get_path_length(code, depth, maxdepth):
    total_length = 0
    current_char = "A"

    for char in code:
        possible_routes = DIRECTIONAL_POSSIBLE_ROUTES[current_char][char]

        if depth == maxdepth:
            total_length += len(min(possible_routes, key=len))
        else:
            lengths = set()
            for route in possible_routes:
                lengths.add(get_path_length(route, depth + 1, maxdepth))
            total_length += min(lengths)

        current_char = char

    return total_length


solution_1 = 0
solution_2 = 0
for code in codes:
    code_int = int(code[:-1])
    numerics = get_numeric_paths("A" + code, 0, set())

    lengths = set()
    for numeric in numerics:
        lengths.add(get_path_length(numeric, 1, 2))

    solution_1 += code_int * min(list(lengths))

    lengths = set()
    for numeric in numerics:
        lengths.add(get_path_length(numeric, 1, 26))
    solution_2 += code_int * min(list(lengths))

print("Solution 1 - ", solution_1)
print("Solution 2 - ", solution_2)

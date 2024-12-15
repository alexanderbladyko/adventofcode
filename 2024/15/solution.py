# https://adventofcode.com/2024/day/15

from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    map_str, moves_str = f.read().split("\n\n")

start = 0, 0
grid = []
double_grid = []
for y, row in enumerate(map_str.split("\n")):
    grid.append([c for c in row])
    for x, c in enumerate(row):
        if c == "@":
            start = (x, y)
            grid[y][x] = "."
    double_grid.append([])
    for x, char in enumerate(row):
        if char == "#":
            double_grid[y].append("#")
            double_grid[y].append("#")
        elif char == ".":
            double_grid[y].append(".")
            double_grid[y].append(".")
        elif char == "O":
            double_grid[y].append("[")
            double_grid[y].append("]")
        elif char == "@":
            double_grid[y].append(".")
            double_grid[y].append(".")


DIRECTION_BY_SYMBOL = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, -1),
    "v": (0, 1),
}

moves = []
for row in moves_str.split("\n"):
    for char in row:
        moves.append(DIRECTION_BY_SYMBOL[char])


def print_grid(x, y):
    for ry, row in enumerate(grid):
        for rx, char in enumerate(row):
            print("@" if (rx, ry) == (x, y) else char, end="")
        print()
    print()


x, y = start

for dx, dy in moves:
    blocks_to_move = []
    mx, my = x, y
    while grid[my][mx] != "#":
        mx += dx
        my += dy
        if grid[my][mx] == ".":
            x += dx
            y += dy
            for bx, by in blocks_to_move:
                grid[by][bx] = "."
            for bx, by in blocks_to_move:
                grid[by + dy][bx + dx] = "O"
            break
        if grid[my][mx] == "O":
            blocks_to_move.append((mx, my))


solution_1 = 0
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == "O":
            solution_1 += 100 * y + x

print("Solution 1 - ", solution_1)


grid = double_grid

x, y = start[0], start[1] * 2

BOX_FORCES = {
    (1, 0): {
        "[": [(1, 0)],
    },
    (-1, 0): {
        "]": [(-1, 0)],
    },
    (0, -1): {"[": [(0, 0), (1, 0)], "]": [(-1, 0), (0, 0)]},
    (0, 1): {"[": [(0, 0), (1, 0)], "]": [(-1, 0), (0, 0)]},
}


def collect_boxes_to_move(grid, from_position, direction):
    px, py = from_position[0] + direction[0], from_position[1] + direction[1]
    if grid[py][px] == ".":
        return set(), True
    if grid[py][px] == "#":
        return set(), False
    if grid[py][px] in BOX_FORCES[direction]:
        boxes = set()
        boxes.add((px, py) if grid[py][px] == "[" else (px - 1, py))
        can_move = True
        for fx, fy in BOX_FORCES[direction][grid[py][px]]:
            new_boxes, can_move_boxes = collect_boxes_to_move(
                grid, (px + fx, py + fy), direction
            )
            boxes = boxes.union(new_boxes)
            can_move = can_move and can_move_boxes
        return boxes, can_move
    raise RuntimeError("Should not come here")


robot = (start[0] * 2, start[1])
for direction in moves:
    boxes, can_move = collect_boxes_to_move(grid, robot, direction)
    if can_move:
        robot = (robot[0] + direction[0], robot[1] + direction[1])
        for box in boxes:
            grid[box[1]][box[0]] = "."
            grid[box[1]][box[0] + 1] = "."
        dx, dy = direction
        for box in boxes:
            grid[box[1] + dy][box[0] + dx] = "["
            grid[box[1] + dy][box[0] + dx + 1] = "]"
    # print_grid(robot[0], robot[1])

solution_2 = 0
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == "[":
            solution_2 += 100 * y + x

print("Solution 2 - ", solution_2)

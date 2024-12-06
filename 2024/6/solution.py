# https://adventofcode.com/2024/day/6

import time
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

N = len(lines)
M = len(lines[0])


DIRECTIONS = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]

direction = 0

solution_2 = 0


def start_pos():
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "^":
                return (j, i)
    assert False


positions = set()
x, y = start_pos()
positions.add((x, y))

while True:
    dx, dy = DIRECTIONS[direction]
    nx, ny = x + dx, y + dy

    if not (0 <= nx < M and 0 <= ny < N):
        break

    if lines[ny][nx] == "#":
        direction = (direction + 1) % len(DIRECTIONS)
    else:
        x, y = nx, ny
        positions.add((x, y))


def check_loop(obstruction):
    positions = set()
    direction = 0
    x, y = start_pos()
    positions.add((x, y, direction))

    while True:
        dx, dy = DIRECTIONS[direction]
        nx, ny = x + dx, y + dy

        if not (0 <= nx < M and 0 <= ny < N):
            return False

        if lines[ny][nx] == "#" or (nx, ny) == obstruction:
            direction = (direction + 1) % len(DIRECTIONS)
        else:
            if (nx, ny, direction) in positions:
                # print(nx, ny, direction)
                return True
            x, y = nx, ny
            positions.add((x, y, direction))


# Used to debug
# p = Path(__file__).with_name("output.txt")
# with p.open("w") as f:
#     for i, line in enumerate(lines):
#         f.write(
#             "".join("X" if (j, i) in positions else char for j, char in enumerate(line))
#         )


start = time.time()
for position in list(positions):
    if check_loop(position):
        solution_2 += 1

end = time.time()

print("Solution 1 - ", len(positions))
print("Time of solution 2", end - start)
print("Solution 2 - ", solution_2)

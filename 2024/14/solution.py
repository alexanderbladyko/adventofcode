# https://adventofcode.com/2024/day/14

from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

robots = []
for line in lines:
    point, vector = line.split(" ")
    robots.append(
        (
            tuple(int(v) for v in point[2:].split(",")),
            tuple(int(v) for v in vector[2:].split(",")),
        )
    )

N = 101
HALF_N = N // 2
M = 103
HALF_M = M // 2
SECONDS = 100


def get_position(robot, second):
    (px, py), (vx, vy) = robot
    return (px + vx * second) % N, (py + vy * second) % M


def print_space_lines(second):
    grid = []
    for _ in range(M):
        grid.append(["."] * N)

    for robot in robots:
        x, y = get_position(robot, second)
        grid[y][x] = "X"

    for row in grid:
        print("".join(row) + "\n")


def check_no_overlaps(second):
    positions = set()

    for robot in robots:
        x, y = get_position(robot, second)
        if (x, y) in positions:
            return False
        positions.add((x, y))
    return True


quadrants = [[0, 0], [0, 0]]

for robot in robots:
    x, y = get_position(robot, SECONDS)
    if x != HALF_N and y != HALF_M:
        quadrants[0 if x < HALF_N else 1][0 if y < HALF_M else 1] += 1

solution_1 = quadrants[0][0] * quadrants[1][0] * quadrants[0][1] * quadrants[1][1]

print("Solution 1 - ", solution_1)


second = 0
while True:
    second += 1
    if check_no_overlaps(second):
        # print_space_lines(second)
        print("Solution 2 - ", second)
        break

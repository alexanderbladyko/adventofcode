# https://adventofcode.com/2024/day/10

from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.read().split("\n")

N = len(lines)
M = len(lines[0])

solution_1 = 0
solution_2 = 0


def get_trails(prev_value, x, y):
    if not (0 <= x < N and 0 <= y < M):
        return set(), 0
    value = prev_value + 1
    if int(lines[x][y]) != value:
        return set(), 0
    if lines[x][y] == "9":
        return {(x, y)}, 1

    set1, score1 = get_trails(value, x - 1, y)
    set2, score2 = get_trails(value, x, y - 1)
    set3, score3 = get_trails(value, x + 1, y)
    set4, score4 = get_trails(value, x, y + 1)

    return (set1.union(set2).union(set3).union(set4)), score1 + score2 + score3 + score4


for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "0":
            paths, score = get_trails(-1, i, j)
            solution_1 += len(paths)
            solution_2 += score

print(f"Solution 1 - {solution_1}")

print(f"Solution 2 - {solution_2}")

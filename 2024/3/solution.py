# https://adventofcode.com/2024/day/3

import re

from pathlib import Path

MUL_REGEX = re.compile("mul\((\d+),(\d+)\)")
DO_DONT_REGEX = re.compile("(?s)do\(\)(.*?)don't\(\)")


p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    line = f.read().strip()
    D = line

reports = []
solution_1 = 0
solution_2 = 0

groups = MUL_REGEX.findall(line)
for group in groups:
    solution_1 += int(group[0]) * int(group[1])

do_groups = DO_DONT_REGEX.findall("do()" + line)
for group in do_groups:
    groups = MUL_REGEX.findall(group)
    for group in groups:
        solution_2 += int(group[0]) * int(group[1])

print("Solution 1 - ", solution_1)
print("Solution 2 - ", solution_2)

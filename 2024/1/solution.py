# https://adventofcode.com/2024/day/1


from pathlib import Path

from collections import Counter

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

measure_1 = []
measure_2 = []

for line in lines:
    parts = line.split()
    measure_1.append(int(parts[0]))
    measure_2.append(int(parts[1]))


solution_1 = sum(
    abs(left - right) for left, right in zip(sorted(measure_1), sorted(measure_2))
)

print("Solution 1 - ", solution_1)

measure_2_counts = Counter(measure_2)

solution_2 = sum(m * measure_2_counts[m] for m in measure_1)

print("Solution 2 - ", solution_2)

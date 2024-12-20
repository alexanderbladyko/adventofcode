# https://adventofcode.com/2024/day/19

from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    towels_str, patterns_str = f.read().split("\n\n")

towels = towels_str.split(", ")
patterns = patterns_str.split("\n")


def check_pattern(pattern):
    dp = [1] + [0] * len(pattern)
    for i in range(len(pattern)):
        index = i + 1
        for towel in towels:
            if pattern[index - len(towel):index] == towel and dp[index - len(towel)]:
                dp[index] += dp[index - len(towel)]
    return dp[-1]

solution_1 = 0
solution_2 = 0
for pattern in patterns:
    result = check_pattern(pattern)
    if result > 0:
        solution_1 += 1
        solution_2 += result


print("Solution 1 - ", solution_1)
print("Solution 2 - ", solution_2)

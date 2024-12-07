# https://adventofcode.com/2024/day/7

import time
from pathlib import Path
from itertools import product

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()


solution_1 = 0
solution_2 = 0

OPERATIONS_1 = ("+", "*")
OPERATIONS_2 = ("+", "*", "||")

equations = []
for line in lines:
    result, args = line.strip().split(":")
    equations.append((int(result), [int(v) for v in args.strip().split(" ")]))


def is_valid(equation, possible_operations):
    result, args = equation
    perms = list(product(possible_operations, repeat=len(args) - 1))
    for operations in perms:
        expression = args[0]
        for i, operation in enumerate(operations):
            match operation:
                case "+":
                    expression += args[i + 1]
                case "*":
                    expression *= args[i + 1]
                case "||":
                    expression = (
                        expression * (10 ** len(str(args[i + 1]))) + args[i + 1]
                    )
        if expression == result:
            return True
    return False


start = time.time()
for equation in equations:
    if is_valid(equation, OPERATIONS_1):
        solution_1 += equation[0]
end = time.time()
print(f"Solution 1 - {solution_1}. Time - {end - start}")

start = time.time()
for equation in equations:
    if is_valid(equation, OPERATIONS_2):
        solution_2 += equation[0]
end = time.time()
print(f"Solution 2 - {solution_2}. Time - {end - start}")

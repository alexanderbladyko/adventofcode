# https://adventofcode.com/2024/day/24

from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    inputs_str, operations_str = f.read().split("\n\n")

values = dict()
for line in inputs_str.split("\n"):
    name, value = line.split(": ")
    values[name] = value == "1"

operations = []
for op_str in operations_str.split("\n"):
    left, op, right, _, result = op_str.split(" ")
    operations.append((left, right, op, result))

max_z = 0

calculated = set()
while True:
    processed = 0
    for left, right, operation, result in operations:
        if left not in values or right not in values:
            continue
        if (left, right, result) in calculated:
            continue
        calculated.add((left, right, result))
        if result.startswith("z"):
            max_z = max(max_z, int(result[1:]))
        processed += 1
        match operation:
            case "OR":
                values[result] = values[left] or values[right]
            case "AND":
                values[result] = values[left] and values[right]
            case "XOR":
                values[result] = values[left] != values[right]
    if processed == 0:
        break

solution_1 = ""
for i in reversed(
    range(
        max_z + 1,
    )
):
    solution_1 += "1" if values[f"z{i:02}"] else "0"


print("Solution 1 - ", int(solution_1, 2))

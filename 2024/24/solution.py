# https://adventofcode.com/2024/day/24

from pathlib import Path


p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    inputs_str, operations_str = f.read().split("\n\n")

values = dict()
for line in inputs_str.split("\n"):
    name, value = line.split(": ")
    values[name] = int(value)

operations = []
for op_str in operations_str.split("\n"):
    left, op, right, _, result = op_str.split(" ")
    operations.append((left, right, op, result))


def get_value(values, startswith):
    filtered_values = {
        name: value for name, value in values.items() if name.startswith(startswith)
    }
    sorted_values = sorted(filtered_values.items())
    binary_string = ""
    for i, (name, value) in enumerate(sorted_values):
        if int(name[1:]) != i:
            return False, 0
        binary_string += str(value)
    # print("%70s" % binary_string[::-1])
    return True, int(binary_string[::-1], 2)


def calculate(values, operations, swaps):
    exit_values = values.copy()
    calculated = set()
    while True:
        processed = 0
        for left, right, operation, output in operations:
            real_output = swaps.get(output, output)

            if left not in exit_values or right not in exit_values:
                continue
            if (left, right, real_output) in calculated:
                continue
            calculated.add((left, right, real_output))
            processed += 1
            match operation:
                case "OR":
                    exit_values[real_output] = exit_values[left] | exit_values[right]
                case "AND":
                    exit_values[real_output] = exit_values[left] & exit_values[right]
                case "XOR":
                    exit_values[real_output] = exit_values[left] ^ exit_values[right]
        if processed == 0:
            break
    return exit_values


calculation = calculate(values, operations, swaps={})
get_value(calculation, "x")
get_value(calculation, "y")
_, solution_1 = get_value(calculation, "z")
# print_operations(operations, {}, calculation, "input")
print("Solution 1 - ", solution_1)


XOR = "XOR"
AND = "AND"
OR = "OR"

gates = {}
replace_gates = {}


def minmax(a, b):
    return (min(a, b), max(a, b))


for left, right, operation, output in operations:
    left, right = minmax(left, right)
    gates[left, right, operation] = output
    replace_gates[output] = left, right, operation


def swap(a, b):
    replace_gates[a], replace_gates[b] = replace_gates[b], replace_gates[a]
    gates[replace_gates[a]], gates[replace_gates[b]] = (
        gates[replace_gates[b]],
        gates[replace_gates[a]],
    )


output = set()
c = ""
for i in range(int(max(replace_gates)[1:])):
    x = f"x{i:02}"
    y = f"y{i:02}"
    z = f"z{i:02}"
    xxory = gates[x, y, XOR]
    xandy = gates[x, y, AND]
    if not c:
        c = xandy
    else:
        a, b = minmax(c, xxory)
        k = a, b, XOR
        if k not in gates:
            a, b = list(set(replace_gates[z][:2]) ^ set(k[:2]))
            output.add(a)
            output.add(b)
            swap(a, b)
        elif gates[k] != z:
            output.add(gates[k])
            output.add(z)
            swap(z, gates[k])
        k = replace_gates[z]
        xxory = gates[x, y, XOR]
        xandy = gates[x, y, AND]
        c = gates[*minmax(c, xxory), AND]
        c = gates[*minmax(c, xandy), OR]

print("Solution 2 - ", ",".join(sorted(output)))

# https://adventofcode.com/2024/day/17

from pathlib import Path


p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

A = 0
B = 1
C = 2

commands_str = lines[4].split(": ")[1]

commands = [int(v) for v in commands_str.split(",")]


def get_operand_value(reg, operand):
    if 0 <= operand <= 3:
        return operand
    return reg[operand - 4]


def perform(reg, opcode, operand, instruction_pointer):
    if opcode == 0:
        reg[A] //= 2 ** get_operand_value(reg, operand)
    elif opcode == 1:
        reg[B] ^= get_operand_value(reg, operand)
    elif opcode == 2:
        reg[B] = get_operand_value(reg, operand) % 8
    elif opcode == 3:
        if reg[A] != 0:
            return get_operand_value(reg, operand), ""
    elif opcode == 4:
        reg[B] ^= reg[C]
    elif opcode == 5:
        return instruction_pointer + 2, str(get_operand_value(reg, operand) % 8)
    elif opcode == 6:
        reg[B] = reg[A] // (2 ** get_operand_value(reg, operand))
    elif opcode == 7:
        reg[C] = reg[A] // (2 ** get_operand_value(reg, operand))

    return instruction_pointer + 2, ""


# instruction_pointer = 0
# output = []

# reg = [int(line.split(": ")[1]) for line in lines[0:3]]
# while instruction_pointer < len(commands) - 1:
#     instruction_pointer, new_output = perform(
#         reg,
#         commands[instruction_pointer],
#         commands[instruction_pointer + 1],
#         instruction_pointer,
#     )
#     if new_output:
#         output.append(new_output)


# print("Solution 1 - ", ','.join(output))


# Brute force


def check_value(init_A):
    check_reg = [init_A, 0, 0]
    limit = 500
    count = 0

    pointer = 0
    check_output = []

    while pointer < len(commands) - 1 and count <= limit:
        pointer, new_output = perform(
            check_reg,
            commands[pointer],
            commands[pointer + 1],
            pointer,
        )
        if new_output:
            if str(commands[len(check_output)]) != new_output:
                return False
            check_output.append(new_output)
        count += 1
    return ",".join(check_output) == commands_str


solution_2 = 0
for i in range(2393052000, 3000000000):
    if i % 1000 == 0:
        print(i)
    if check_value(i):
        solution_2 = i
        break

print("Solution 2 - ", solution_2)

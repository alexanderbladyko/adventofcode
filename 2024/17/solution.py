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
            return get_operand_value(reg, operand), []
    elif opcode == 4:
        reg[B] ^= reg[C]
    elif opcode == 5:
        return instruction_pointer + 2, [get_operand_value(reg, operand) % 8]
    elif opcode == 6:
        reg[B] = reg[A] // (2 ** get_operand_value(reg, operand))
    elif opcode == 7:
        reg[C] = reg[A] // (2 ** get_operand_value(reg, operand))

    return instruction_pointer + 2, []


instruction_pointer = 0
output = []

reg = [int(line.split(": ")[1]) for line in lines[0:3]]
while instruction_pointer < len(commands) - 1:
    instruction_pointer, new_output = perform(
        reg,
        commands[instruction_pointer],
        commands[instruction_pointer + 1],
        instruction_pointer,
    )
    if new_output:
        output.extend(new_output)


print("Solution 1 - ", ','.join(map(str, output)))


def exec_commands(regs, commands):
    pointer = 0
    output = []

    while pointer < len(commands) - 1:
        pointer, new_output = perform(
            regs,
            commands[pointer],
            commands[pointer + 1],
            pointer,
        )
        if new_output:
            output.extend(new_output)
    return output


# I've stole this one. Too hard for me
def find_register_a_for_self_output(registers, commands):
    numbers = []
    todo = [(len(commands) - 1, 0)]  # Start from the last position of the program with value '0'
    for p, v in todo:
        # Test all possible values of 'a' within the range [8*v, 8*(v+1) - 1] --> 2^3 = 8 (cause 3 bits computer)
        for a in range(8 * v, 8 * (v + 1)):
            # Check if running the program with the current 'a' produces the remaining part of the program
            if exec_commands([a, registers[1], registers[2]], commands) == commands[p:]:
                if p == 0:  # If we're at the start of the program, we've found a valid 'a'
                    numbers.append(a)
                else:
                    # Otherwise, move one step back and continue searching for valid 'a' values
                    todo += [(p - 1, a)]
    # Return the smallest valid 'a' that satisfies the condition
    return min(numbers)


solution_2 = find_register_a_for_self_output(reg, commands)

print("Solution 2 - ", solution_2)

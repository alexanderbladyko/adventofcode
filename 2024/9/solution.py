# https://adventofcode.com/2024/day/9

from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    line = f.read()

solution_1 = 0
final_size = 0

stack = []

for i, char in enumerate(line):
    if i % 2 == 0:
        count = int(char)
        final_size += count
        stack.extend([int(i / 2)] * count)


index = 0
for i, char in enumerate(line):
    count = int(char)
    for j in range(count):
        if not stack:
            break
        solution_1 += index * stack.pop(0 if i % 2 == 0 else -1)
        index += 1
    if index >= final_size:
        break

print(f"Solution 1 - {solution_1}")

solution_2 = 0
files = []

index = 0
for i, char in enumerate(line):
    files.append((int(char), int(i / 2) if i % 2 == 0 else "_"))


used = set()

for file_index in range(len(files) - 1, 0, -1):
    file = files[file_index]
    if file[1] != "_" and file not in used:
        used.add(file)
        for i, space in enumerate(files):
            if i >= file_index:
                break

            if space[1] == "_":
                if space[0] == file[0]:
                    files[i], files[file_index] = files[file_index], files[i]
                    break
                elif space[0] > file[0]:
                    remaining = space[0] - file[0]
                    files[i], files[file_index] = file, (file[0], "_")
                    files.insert(i + 1, (remaining, "_"))
                    break

index = 0
for size, value in files:
    if value != "_":
        for i in range(0, size):
            solution_2 += (index + i) * value
    index += size


print(f"Solution 2 - {solution_2}")

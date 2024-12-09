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


# index = 0
# for i, char in enumerate(line):
#     count = int(char)
#     for j in range(count):
#         if not stack:
#             break
#         solution_1 += index * stack.pop(0 if i % 2 == 0 else -1)
#         index += 1
#     if index >= final_size:
#         break

solution_2 = 0
files = []
spaces = []
index = 0
for i, char in enumerate(line):
    size = int(char)
    if i % 2 == 0:
        files.append((index, size, int(i / 2)))
    else:
        spaces.append((index, size))
    index += size



# for i in range(len(files) - 1, 0, -1):
#     file_index, file_size, value = files.pop()

#     index = -1
#     for j in range(0, i - 1):
#         left_index, left_size, _ = files[j]
#         right_index, _, _ = files[j + 1]
#         # Can insert
#         if left_index + left_size + file_size <= right_index:
#             index = j
#             i += 1
#             break
#     files.insert(index + 1, (files[index][0] + files[index][1], file_size, value))






# print(files)


print(f"Solution 1 - {solution_1}")
print(f"Solution 2 - {solution_2}")

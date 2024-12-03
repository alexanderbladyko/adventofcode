# https://adventofcode.com/2024/day/2


from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

reports = []
for line in lines:
    reports.append([int(p) for p in line.split()])


def is_save(report):
    is_asc = report[0] < report[1]

    for first, second in zip(report, report[1:]):
        if is_asc and first > second:
            return False
        if not is_asc and first < second:
            return False
        diff = abs(first - second)
        if diff == 0 or diff > 3:
            return False
    return True


def is_save_without_one(report):
    if is_save(report):
        return True
    for i in range(len(report)):
        if is_save(report[:i] + report[i + 1 :]):
            return True
    return False


solution_1 = sum(1 for report in reports if is_save(report))
print("Solution 1 - ", solution_1)

solution_2 = sum(1 for report in reports if is_save_without_one(report))
print("Solution 2 - ", solution_2)

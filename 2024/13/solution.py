# https://adventofcode.com/2024/day/13

from pathlib import Path
import z3

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    blocks = f.read().split("\n\n")

plays = []
for block in blocks:
    buttonA, buttonB, result = block.split("\n")
    a = tuple(int(v[1:]) for v in buttonA[10:].split(", "))
    b = tuple(int(v[1:]) for v in buttonB[10:].split(", "))
    prize = tuple(int(v[2:]) for v in result[7:].split(", "))
    plays.append((a, b, prize))


A_TOKENS = 3
B_TOKENS = 1

TASK_2_ADDITION = 10000000000000


def get_tokens(play, max_count=None):
    a, b, prize = play

    ax, ay = a
    bx, by = b
    px, py = prize

    a = z3.Int("a")
    b = z3.Int("b")

    solver = z3.Solver()

    solver.add(ax * a + bx * b == px)
    solver.add(ay * a + by * b == py)

    solver.add(a >= 0)
    solver.add(b >= 0)
    if max_count:
        solver.add(a <= max_count)
        solver.add(b <= max_count)

    found = False
    tokens = 0

    while solver.check() == z3.sat:
        model = solver.model()
        new_a = model[a].as_long()
        new_b = model[b].as_long()
        new_tokens = A_TOKENS * new_a + B_TOKENS * new_b

        if tokens < new_tokens or not found:
            found = True
            tokens = new_tokens

        solver.add(z3.Or(a != new_a, b != new_b))

    return tokens, found


solution_1 = 0
solution_2 = 0

for play in plays:
    tokens, found = get_tokens(play, max_count=100)
    if found:
        solution_1 += tokens

    a, b, prize = play
    tokens, found = get_tokens(
        (a, b, (TASK_2_ADDITION + prize[0], TASK_2_ADDITION + prize[1]))
    )
    if found:
        solution_2 += tokens

print("Solution 1 - ", solution_1)
print("Solution 2 - ", solution_2)

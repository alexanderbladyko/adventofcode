# https://adventofcode.com/2024/day/22

from pathlib import Path
from collections import defaultdict

MODULO = 16777216

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    secret_numbers = [int(v) for v in f.read().split("\n")]


def simulate_secret_number(secret):
    for _ in range(2000):
        secret ^= (secret * 64) % MODULO
        secret ^= (secret // 32) % MODULO
        secret ^= (secret * 2048) % MODULO
    return secret


def get_price_changes(secret):
    prices = []
    for _ in range(2000):
        price = secret % 10
        prices.append(price)

        secret ^= (secret * 64) % MODULO
        secret ^= (secret // 32) % MODULO
        secret ^= (secret * 2048) % MODULO
        secret %= MODULO

    changes = []
    for i in range(1, len(prices)):
        changes.append(prices[i] - prices[i - 1])

    return prices, changes


def get_bananas(secrets):
    sequence_prices = defaultdict(int)
    for secret in secrets:
        prices, changes = get_price_changes(secret)
        visited = set()
        for i in range(len(changes) - 3):
            seq = tuple(changes[i : i + 4])
            if seq not in visited:
                visited.add(seq)
                sequence_prices[seq] += prices[i + 4] % 10
    return max(sequence_prices.values())


solution_1 = sum(simulate_secret_number(v) for v in secret_numbers)
print("Solution 1 - ", solution_1)
print("Solution 2 - ", get_bananas(secret_numbers))

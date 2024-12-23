# https://adventofcode.com/2024/day/23

from pathlib import Path
from collections import defaultdict

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    pairs = [tuple(v.split("-")) for v in f.read().split("\n")]

graph = defaultdict(set)
for left, right in pairs:
    graph[left].add(right)
    graph[right].add(left)


triplets = set()

for first, links in graph.items():
    connected = list(links)
    for i in range(len(connected) - 1):
        for j in range(i + 1, len(connected)):
            if connected[j] in graph[connected[i]]:
                triplets.add(tuple(sorted([first, connected[i], connected[j]])))


solution_1 = 0

for triplet in triplets:
    if any(t.startswith("t") for t in triplet):
        solution_1 += 1


# thanks to ChatGPT
def bron_kerbosch(r, p, x, graph, cliques):
    """
    Implementation of the Bron-Kerbosch algorithm for finding all maximal cliques in a graph.

    :param r: Current clique (set of vertices)
    :param p: Vertices that can be added to the current clique
    :param x: Vertices that cannot be added to the current clique
    :param graph: Adjacency list representation of the graph
    :param cliques: List to store the found cliques
    """
    if not p and not x:
        cliques.append(r)
        return

    for vertex in list(p):
        bron_kerbosch(
            r.union({vertex}),
            p.intersection(graph[vertex]),
            x.intersection(graph[vertex]),
            graph,
            cliques,
        )
        p.remove(vertex)
        x.add(vertex)


def find_maximum_clique(graph):
    """
    Find the maximum clique in a graph.

    :param graph: Adjacency list representation of the graph
    :return: The maximum clique
    """
    cliques = []
    bron_kerbosch(set(), set(graph.keys()), set(), graph, cliques)
    max_clique = max(cliques, key=len)
    return max_clique


solution_2 = find_maximum_clique(graph)
print("Solution 1 - ", solution_1)
print("Solution 2 - ", ",".join(sorted(solution_2)))

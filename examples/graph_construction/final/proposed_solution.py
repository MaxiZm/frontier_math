"""Final candidate: the complete bipartite graph K_{3,3} on vertices 0..5.

K_{3,3} is triangle-free and has 9 edges -- optimal for n=6 by Mantel's theorem
(max triangle-free edges = floor(n^2 / 4) = 9). A deterministic finite loop
builds the explicit edge list, which is allowed by the compliance rules.
"""


def solve():
    left = [0, 1, 2]
    right = [3, 4, 5]
    edges = []
    for u in left:
        for v in right:
            edges.append([u, v])
    return edges

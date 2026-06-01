# Triangle-free graph with the most edges on 6 vertices

Construct a simple, triangle-free graph on the 6 vertices `{0, 1, 2, 3, 4, 5}`
with as many edges as possible. Beat the baseline of 8 edges.

By Mantel's theorem the maximum is `floor(6^2 / 4) = 9`, achieved by the
complete bipartite graph `K_{3,3}`.

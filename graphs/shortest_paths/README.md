# Shortest Paths

In a shortest path problem we are given a **weighted directed graph**. The weight
 of a path is the sum of weights of all of its constituent edges. Shortest path
 (defined by *∂(u, v)*) is defined by a minimum path weight, that is if a path
 *u -> v* exists, or by infinity otherwise. Note that edge weights can represent
 different metrics, not just the distance.

Shortest-paths algorithms rely on the property that shortest path contains other
 shortest sub-paths within it. Some graphs may include edges whose weights are
 negative, so the shortest path in this graph would include more edges than its
 non-negative counterpart. Shortest path cannot contain a cycle, and some
 algorithms can detect and report their existence.

Shortest path is represented by a tree of vertex predecessors (as in breadth-
 first tree). Weight of a path to a vertex equals the sum of weights of all the
 edges that have led to the vertex. Vertex predecessor is another vertex with
 which it shares the most relaxed edge. If we follow parent records in a
 predecessor-tree all the way to the starting vertex after search was finished,
 we'll get the shortest route it would take to reach the destination vertex.

Algorithms in this module cover solutions to single-source shortest paths problem.
 They share technique of initialization, edge relaxation and shortest-path
 estimation. Other powerful method worth mentioning is a bidirectional search
 (not implemented here). Longest path can be calculated by negating weights.
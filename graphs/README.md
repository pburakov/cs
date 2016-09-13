# Graph

Graph is a linked data structure comprised of **vertices** (nodes or points) and 
 **edges** (lines, arrows or arcs) representing relationships between vertices.

Graphs can be directed and undirected, their edges can form cycles. Sometimes a vertex can
 point to itself. **Directed acyclic graph** is often short-named DAG.

The number of outgoing edges a vertex has is called a vertex **degree**. Every finite
 undirected graph has an even number of vertices with odd degree. This is so called
 *handshaking lemma*, so named due to a notorious example. In a party of people some
 of whom shake hands, an even number of people must have shaken an odd number of other
 people's hands.

There are several ways to represent a graph. Most commonly used are **adjacency list**
 (map) and **adjacency matrix** (2D array) representations. This implementation uses
 vertex and edge objects with a combination of adjacency maps.

Adjacency list can be used to represent both directed and **undirected graph** types.
 For an undirected graph, relation between adjacent vertices is always mutual, while
 in a directed graph, it is not necessarily the case.
 
###See code:
- [Graph Representation](./__init__.py)
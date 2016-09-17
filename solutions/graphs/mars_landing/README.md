# Mars Lander

Imagine you are sending a lander to Mars. Your lander has *p* probes on-board that can
 travel the shortest route at constant speed to designated points of interest for a
 scientific survey and then back following the same path. You are given a map of surface
 sized *m*x*n*, where `-` are normal tiles and `x` are rocky tiles that are impassable.
 You are also given *p* sets of coordinates *P* for all your probes. Your probes can move
 to adjacent horizontal and vertical tile, consuming 1 unit of fuel on every move. Find
 such a landing position for your lander so that the fuel consumption for all *p* probes
 is minimal. Assume that all points are reachable (not blocked by rocks).

Example:
```
p=3; P=[(0, 0), (0, 3), (3, 1)]
M = [
    ['-', 'x', 'x', '-'],
    ['-', '-', 'x', '-'],
    ['-', '-', '-', '-'],
    ['-', '-', '-', '-'],
]
Best landing site: (2, 1).
```
I was given this problem when I was interviewing at Google. Here is my stab at it.


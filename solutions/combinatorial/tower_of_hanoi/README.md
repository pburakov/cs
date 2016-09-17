# Tower of Hanoi

Tower of Hanoi is a classic problem that is often used to demonstrate recursion.
 Exact conditions are described [here](https://en.wikipedia.org/wiki/Tower_of_Hanoi).

Solution algorithm for two disks is simple. Let *A* be the original rod, *B* the destination and
 *C* the auxiliary rod. Problem can be solved in following steps.
 1. pick from *A*, put on *C*
 2. pick another disk from *A*, put directly onto *B*
 3. pick disk from *C*, put on *B*

###See code:
- [Solution](./__init__.py)
- [Driver](./driver.py)
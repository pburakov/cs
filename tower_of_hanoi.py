"""
This is a simple recursive solution for Tower Of Hanoi puzzle.
 More info: https://en.wikipedia.org/wiki/Tower_of_Hanoi
"""


def move_tower(h, from_pole, to_pole, with_pole):
    """
    Initiates a recursive Tower Of Hanoi algorithm to move h disks between
     first two poles via the third pole.
    The set of required actions is printed to the console.
    Caution: number of actions grows exponentially for each step of h. Use of larger
     h values may overwhelm the output.
    :param h: Height of the original (ordered) pyramid
    """
    if h >= 1:
        move_tower(h - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(h - 1, with_pole, to_pole, from_pole)


def move_disk(fp, tp):
    """
    Prints the moving action.
    """
    print("moving disk from", fp, "to", tp)


move_tower(5, "A", "B", "C")

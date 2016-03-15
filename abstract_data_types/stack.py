from abstract_data_types.linked_list import Node as Item


class Stack:
    """
    Implementation of Stack (last in first out) data type.

    Stack:
        4 -> [5, 6, 7]
        4 <- [4, 5, 6, 7]

    """

    def __init__(self):
        self.first = None

    def add(self, item):
        if self.first is not None:
            item.next = self.first
        self.first = item

    def peek(self):
        return self.first

    def pop(self):
        if self.first is None:
            raise ValueError("Empty stack")
        output = self.first
        self.first = self.first.next
        return output

    def is_empty(self):
        return self.first is None

    def size(self):
        next = self.first
        counter = 0
        while next is not None:
            counter += 1
            next = next.next
        return counter

    def __str__(self):
        next = self.first
        items = []
        while next is not None:
            items.append(next.value)
            next = next.next
        tostr = ', '.join(items)
        return "[{}]".format(tostr)


a = Item('a')
b = Item('b')
c = Item('c')
d = Item('d')
e = Item('e')
stack = Stack()
stack.add(a)
stack.add(b)
stack.add(c)
stack.add(d)
stack.add(e)
print(stack)
print("Size: ", stack.size())
print("Peek: ", stack.peek())
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)

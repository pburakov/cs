class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    """
    Linked List is a sequence of Nodes with some value and a reference to
     a next item. Node that is in a beginning of a linked list is referenced
     as Head.

    If a Node has no reference to a next item the it's the last Node
     on the list. Linked list has no index.
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        """
        Has specific implementations
        """
        pass

    def size(self):
        """
        Traversing the list and counting all items from the Head
         until reaching the end of the list.
        Complexity: O(n)
        """
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        return counter

    def search(self, needle):
        """
        Has specific implementations
        """
        pass

    def remove(self, needle):
        """
        Similar to size() and search(). Traverses the list until a match
         is found. Skips current item by unchaining the found Node. Links
         previous item to another Node, unless it's a Head.
        Complexity: worst O(n), best O(1)
        """
        previous = None
        current = self.head
        while current:
            if current.data == needle:
                break
            else:
                previous = current
                current = current.next
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def __str__(self):
        current = self.head
        output = '['
        while current:
            output += str(current.data)
            current = current.next
        return output + ']'


class UnorderedList(List):
    """
    List (Unordered) is a basic representation of a Linked List.

    Unordered linked list:
     [123][Head] -> [196][] -> [12][] -> ... -> [99][E] ->|||
    """

    def add(self, item):
        """
        Creating a new Node and putting it in a beginning of a list,
         keeping a reference to the old Head as a next item.
        Complexity: O(1)
        """
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def search(self, needle):
        """
        Similar to size(). Traverses the list until finds a matching
         Node. Returns True if needle is found.
        Complexity: worst O(n), best O(1)
        """
        current = self.head
        while current:
            if current.data == needle:
                return True
            else:
                current = current.next
        return False


class OrderedList(List):
    """
    Ordered list introduces a relation between neighbouring Nodes.
    This is list is ordered from min to max value.

    Ordered linked list:
     [12][Head] -> [14][] -> [22][] -> ... -> [99][E] ->|||
    """

    def search(self, needle):
        """
        One of the advantages of an Ordered List, compared to Unordered List,
         is that traversing may stop once it's apparent that we've got
         past a value we are looking for meaning that following values will
         only be greater.
         Complexity: worst O(n), best O(1)
        """
        current = self.head
        while current:
            if current.data == needle:
                return True
            else:
                if current.data > needle:
                    return False
                else:
                    current = current.getNext()
        return False

    def add(self, item):
        """
        Unlike the Unordered List, this addition algorithm assures that an
         item being added is placed in the right position of an Ordered List.
         Once the previous Node is found, it unchains it from the next Node
         and places a new Node between the two.
        Addition to the Head is similar to that of Unordered List.
        Complexity: worst O(n), best O(1)
        """
        current = self.head
        previous = None
        while current:
            if current.data > item:
                break
            else:
                previous = current
                current = current.next
        new_node = Node(item)
        if previous is None:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = current
            previous.next = new_node

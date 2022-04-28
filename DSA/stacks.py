
""" Implementing a Stack using a list"""
class Stack:
    def __init__(self):
        self.items = list()

    #returns the length of the stack
    def __len__(self):
        return len(self.items)

    # returns True if the stack is empty or False otherwise
    def is_empty(self):
        assert len(self.items) == 0

    # adds an item to the top of the stack
    def push(self, value):
        self.items.append(value)

    # removes and return the top of the stack
    def pop(self, value):
        assert not self.is_empty()
        return self.items.pop()

    # simply returns the item at the top of the stack
    def peek(self):
        assert not self.is_empty()
        return self.items[-1]


""" Implementation of a Stack using linked list """

# a class to create the linked list
class _StackNode:
    def _init__(self, item, link):
        self.item = item
        self.next = link

class _Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.top is None

    def push(self, value):
        self.top = _StackNode(value, self.top) # create a new stack node
        self.size += 1

    def pop(self):
        assert not self.is_empty()
        node = self.top
        self.top = self.top.next
        self.size -= 1
        return node.item

    def peek(self):
        assert not self.is_empty()
        return self.top.item





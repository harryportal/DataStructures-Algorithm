class QueueNode:
    def __init__(self, val:int):
        self.val = val
        self.next = None


class Queue:
    """ implemeting a list using a python list"""
    def __int__(self):
        self.list = list()

    def isEmpty(self):
        return len(self.list) == 0

    def enque(self, item):
        self.list.append(item)

    # remove and return the first element
    def deque(self):
        assert not self.isEmpty()
        return self.list.pop(0)

class QueueLinked:
    """ implementation using a linked list, This uses a head and tail reference to append and pop items from
    the linked list """

    def __init__(self):
        self.top = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return self.top is None

    def __len__(self):
        return self.count

    def enqueu(self, item):
        # adds an item to the queue
        new_node = QueueNode(val=item)
        if self.isEmpty():
            """ the top and tail parameters should point to the same node for a new queue """
            self.top = self.tail = new_node
        else:
            self.tail.next = new_node
        # adjust the tail pointer to point to the latest node
        self.tail = new_node
        self.count += 1



    def dequeu(self):
        """ first check if the queue is not empty, store the head pointer data,
            and set the head pointe to it next parameter
        """
        assert not self.isEmpty() # verifies if the queue contains at least one queue
        item = self.top
        if self.top is self.tail: # execute this condition if the queue contains a single element
            self.tail = None
        self.top = self.top.next
        self.count -= 1
        return item.data






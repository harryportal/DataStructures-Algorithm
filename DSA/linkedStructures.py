# building a singly linked list
class Link:
    def __init__(self, data):
        self.data = data
        self.next = None


# creating a singly linked list
a = Link(12)
a.next = Link(15)
a.next.next = Link(10)
a.next.next.next = Link(17)


# traversing a linked list with an external reference
def traverse(head):
    curNode = head
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.next


traverse(a)


# searching a linked list
def search(head, target):
    curNode = head
    while curNode is not None and curNode.data != target:
        curNode = curNode.next
    return curNode is not None


print(search(a, 12))

# prepending a node to a linked list
new_node = Link(19)  # create a new node
new_node.next = a  # sets it next to the current head
a = new_node  # make it the new head

traverse(a) # to check the new linked list


def remove_node(head, target):
    # define two external reference
    predNode = None
    curNode = head

    # position the two external reference to your target
    while curNode is not None and curNode.data != target:
        predNode = curNode
        curNode = curNode.next

    # unlink the current Node by setting its previous node to its next node
    if curNode is not None:
        if curNode == head:
            head = curNode.next
        else:
            predNode.next = curNode.next


# implementing an iterator for a linked list
class _Listiterator:
    def __init__(self, listhead):
        self.curnode = listhead  # set the current node to the linked list head

    def __iter__(self):
        return self

    def __next__(self):
        if self.curnode is None:  # gotten to end of the list
            raise StopIteration
        else:
            item = self.curnode.data
            self.curnode = self.curnode.next
            return item


lnklist = _Listiterator(a)
print('#######iterating through a linked list######')
for i in lnklist:
    print(i)

"""
The splitInHalf(head) function, which accepts a head reference to a
singly linked list, splits the list in half and returns the head reference to
the head node of the second half of the list. If the original list contains a
single node, None should be returned.
"""


def splinhalf(head):
    curnode = head  # set the current node to the head
    if curnode.next is None:    # if list contains only one head
        return None

    # find the length of the linked list
    len = 0
    while curnode is not None:
        curnode = curnode.next
        len += 1

    # divide the length of the list by 2
    mid = len // 2

    # traverse to the node in the middle
    count = 0
    curnode = head  # set the current node back to the head
    while count != mid:  # set the current node to the middle node
        curnode = curnode.next
        count += 1

    return curnode.data


print(splinhalf(a))



#search a sorted linked list
def search_sorted(head, target):
    curNode = head
    while curNode is not None and curNode.data < target:
        curNode = curNode.next
    if curNode.data == target:
        return True
    return False # node not in sorted linked list


#adding a node to a sorted linked list, we make use of two external references
def add_node(head, value):
    preNode = None
    curNode = head
    while curNode is not None and value > curNode.data: # find the position to add new value
        preNode = curNode
        curNode = curNode.next
    new_node = Link(value) # create a new node
    new_node.next = curNode
    if curNode == head:
        head = new_node
    else:
        preNode.next = new_node
    return traverse(head)


#deleting a value from a sorted linked list
def delete_sorted(head, target):
    preNode = None
    curNode = head

    while curNode is not None and curNode.data < target:
        preNode = curNode
        curNode = curNode.next

    if curNode is not None:
        if curNode == head:
            head = curNode.next
        else:
            preNode.next = curNode.next
    return traverse(head)

#delete every node from a linked list
def delete_all_node(head):
    curNode = head
    while curNode is not None:
        curNode.data = None
        curNode = curNode.next
    return curNode is None  # should return True
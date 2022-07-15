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

traverse(a)  # to check the new linked list


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
    if curnode.next is None:  # if list contains only one head
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


# search a sorted linked list
def search_sorted(head, target):
    curNode = head
    while curNode is not None and curNode.data < target:
        curNode = curNode.next
    if curNode.data == target:
        return True
    return False  # node not in sorted linked list


# adding a node to a sorted linked list, we make use of two external references
def add_node(head, value):
    preNode = None
    curNode = head
    while curNode is not None and value > curNode.data:  # find the position to add new value
        preNode = curNode
        curNode = curNode.next
    new_node = Link(value)  # create a new node
    new_node.next = curNode
    if curNode == head:
        head = new_node
    else:
        preNode.next = new_node
    return traverse(head)


# deleting a value from a sorted linked list
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


# delete every node from a linked list
def delete_all_node(head):
    curNode = head
    while curNode is not None:
        curNode.data = None
        curNode = curNode.next
    return curNode is None  # should return True


# insert a node after a particular node
def insert_node(prev: Link, new: int):
    new_node = Link(new)
    # set the next paramater of the new node to that of the prev node
    new_node.next = prev.next
    # now set the next of the prev to the new node
    prev.next = new_node


# append to the end of a linked list given the head
def append(head, new_data):
    if head is None:
        head = Link(new_data)
    pointer = head
    # iterate until the last node
    while pointer.next:
        pointer = pointer.next
    pointer.next = new_node


def get_node_lenght(head):
    pointer = head
    count = 0
    while pointer:
        pointer = pointer.next
        count += 1
    return count


# a function to get the nth node from the end of a linked list
def get_node_from_end(head: Link, index):
    pointer = head
    if lenght < index:
        print('Index value greater than the node lenght')
        return None
    # find the lenght of the node
    lenght = get_node_lenght(pointer)
    # iterate up to the l-n position using a for loop
    pointer = head  # set the pointer back to head
    for i in range(0, l - index):
        pointer = pointer.next
    return pointer.data


def get_middle_node(head):
    pointer = head
    lenght = get_node_lenght(pointer)
    mid = lenght // 2
    while mid:
        pointer = pointer.next
        mid -= 1
    return pointer.data


# count the occurence of a given int in a linked list
def get_numberof_value(head, value):
    pointer = head
    count = 0
    while pointer:
        if pointer.data == value:
            count += 1
        pointer = pointer.next
    return count


def detect_loop(head):
    # a function to detect if a loop exists in a linked list
    # i am going to use flood cycle algorithm to solve this
    # create two pointers
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def check_palindrome_linkedlist(head):
    """ The idea here is to use a stack by firt storing all the values of the linked list in a stack
        and then silmotanoulsy iterating through the linked list and popping the stack to compare their values
        . the function would break once the values are different """
    pointer = head
    # fill the stack
    stack = []
    while pointer:
        stack.append(pointer.data)
        pointer = pointer.next
    # iterate through linked list value and compare with stack value
    pointer = head
    while pointer:
        if pointer.data == stack.pop():
            ispalindrom = True
        else:
            ispalindrom = False
            break
    return ispalindrom


def swap_node(head, x, y):
    """ a fucntion to swap the nodes in a linked list"""
    # we first check if either x or y is in present using two external pointer
    prevx = None
    currx = nodex
    while currx and currx.data != x:
        prevx = currx
        currx = currx.next

    prevy = None
    curry = y
    while curry and curry.data != y:
        prevy = curry
        curry = curry.next

    # return false if x or y is not in the list
    if curry is None or currx is None:
        return False

    # check if x or y is the head of the list:
    if prevx is not None:
        prevx.next = curry  # means the node for x is not the head
    else:
        head = curry  # means node x is actually the head

    if prevy is not None:
        prevy.next = currx
    else:
        head = currx

    # swap their next pointers
    curry.next, currx.next = currx.next, curry.next


def find_merge_node(x, y):
    # this is not optimal as it has a runtime of O(n^2)
    if x == y:
        return y  # return either of them as merge point if they're equal
    pointer = x
    while pointer:  # for every node in x, check if any of the node in y matches it
        temp = y
        while temp:
            if pointer == temp:
                return pointer
            temp = temp.next
        pointer = pointer.next
    return None


def find_merge_node_2(x, y):
    # this is a solution to the above implemented using a hash function
    # this solution won't be suitable for long linked list
    if x == y:
        return x
    hash = set()  # a set to store the values of the first node

    while x:
        hash.add(x)
        x = x.next

    while y:
        if y in hash:
            return y
        y = y.next
    return None

def remove_duplicates(head):
    # return the head if the linked list contains only one node
    if head is None or head.next is None:
        return head
    hash = set() # a set to store the linked list data
    pointer = head
    # we append the head data to the set
    hash.add(pointer.data)
    while pointer.next:
        if pointer.next in hash:
            pointer.next = pointer.next.next
        else:
            hash.add(pointer.next.data)
            pointer = pointer.next
    return head





class DoubleLinked:
    """ Keeps track of the previous node to allow reversing easy"""

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedlist:
    def __init__(self):
        self.head = None  # to traverse to the right
        self.last = None  # to traverse to the left

    def add(self, data):
        # the linked list will be empty if the the last node is empty
        if self.last is None:
            self.head = DoubleLinked(data)
            self.last = self.head
        else:
            new_node = DoubleLinked(data)
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node

    def traverse_right(self):
        if self.last is None:
            print("cannot traverse through an empty node")
        pointer = self.head
        while pointer:
            print(pointer.data, end=" ")
            pointer = pointer.next

    def traverse_left(self):
        if self.last is None:
            print("cannot traverse through an empty node")
        pointer = self.last
        while pointer:
            print(pointer.data, end=" ")
            pointer = pointer.prev

# linear sort
def search_unsorted(value, list):
    for i in range(len(list)):
        if list[i] == value:
            return True
    return False


def search_sorted(value, list):
    for i in range(len(list)):
        if list[i] == value:
            return True
        elif list[i] > value:
            return False
        return False


def smallest_value_unsorted(list):
    smallest = list[0]
    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
    return smallest


def binary_search(list, value):
    n = len(list)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if list[mid] == value:
            return True
        elif list[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return False


def bubble_sort(list):
    """ an ineffective sorting algorithm since it has a runtime of O(n^2) due to the inner iterations """
    n = len(list)
    for i in range(n):  # performs an n -1 iteration on the list
        for j in range(0, n -1-i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def selection_sort(list):
    # does an n-1 iteration on the list
    n = len(list)
    for i in range(n - 1):
        # assumes the ith element as the smallest
        temp_smallest = i
        # loops throught the rest elements in the list
        for j in range(i + 1, n):
            if list[j] < list[temp_smallest]:
                temp_smallest = j
        # swap the elements only if the it's not in the proper position
        if temp_smallest != i:
            list[temp_smallest], list[i] = list[i], list[temp_smallest]


def insertion_sort(list):
    n = len(list)
    # assumes the first element is sorted and iterates throught the rest of the list
    for i in range(1, n):
        # store the value to be positioned
        value = list[i]
        # find the postion where the value is to be placed in the ordered part of the list
        position = i
        while position > 0 and value < list[position - 1]:
            list[position] = list[position - 1]
            position -= 1
        list[position] = value


# find the location an item would be placed using binary_search
def find_sorted_position(list, value):
    n = len(list)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == value:
            return mid  # the position of the item
        elif list[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return low # the element can only be placed in the first position at this point


def merge_two_sorted_list(listA, listB):
    """ runtime analysis of 0(n) since it's only performing 2n operations """
    # create an empty list to hold the new list
    merged_list = []
    a = 0
    b = 0  # set a marker for the two list

    # merge the two lists until one is empty
    while a < len(listA) and b < len(listB):
        if listA[a] > listB[b]:
            merged_list.append(listA[a])
            a += 1
        else:
            merged_list.append(listB[b])
            b += 1

    # store the remaining values of the list that stil contains additional items
    while a < len(ListA):
        merged_list.append(listA[a])
        a += 1
    while b < len(listB):
        merged_list.append(listB[b])
        b += 1


class Linked:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def traverse(head: Linked):
    node = head
    while node is not None:
        print(node.data)
        node = node.next


def search(head: Linked, target) -> bool:
    node = head
    while node is not None and node.data != target:
        node = node.next
    return node is not None  # returns False if the item is not in the linked list


def prepend(head: Linked, value: Linked):
    node, value.next, head = head, node, value
    return head


def remove_node(head: Linked, target: Linked):
    # we set two external references
    pre_node = None
    node = head
    while node is not None and node.next != target:
        pre_node = node
        node = node.next
    if node is not None:
        # set the head to the next node incase it's the node to be removed
        if node == head:
            head = node.next
        else:
            pre_node.next = node.next


class LinkedIterator:
    def __init__(self, head: Linked):
        self.node = head

    def __iter__(self):
        return self

    def __next__(self):
        item = self.node.data
        self.node = self.node.next
        return item


def append(head, tail, item):
    # given an external tail and head reference
    new_node = Linked(item)
    if head is None: # creates a new object if head reference is None
        head = new_node
    else:
        tail.next = new_node
    tail = new_node  # the tail is adjusted since it has to be the last node in the linked list


def remove(head, tail, item):
    # remove an item from a linked list given the head and tail references
    pre_node = None
    node = head
    while node is not None and node.data != item:
        pre_node = node
        node = node.next
    if node == head:
        node = head.next
    else:
        pre_node.next = node.next
    if node == tail:
        tail = pre_node


def search_linked(head, target):
    # searchig a sorted linked list
    node = head
    while node is not None and node.data < target:
        node = node.next
    return True if node.data == target else False

def insert_sorted_linked(head, item):
    # this will also make use of two external references
    pre_node = None
    node = head

    while node is not None and node.data < item:
        pre_node = node
        node = node.next
    new_node = Linked(item) # create a new node with the item and set the next parameter to the current node
    new_node.next = node
    if node == head:
        head = new_node
    else:
        pre_node.next = new_node

def remove_sorted_list(head, item):
    pre_node = None
    node = head
    while node is not None and node.data < item:
        pre_node = node
        node = node.next

    if node is not None:
        if node == head:
            head = node.next
        else:
            pre_node.next = node.next



class Stack:
    def __init__(self):
        self.list = list()

    def isEmpty(self):
        return len(self.list) == 0

    def peek(self):
        assert not self.isEmpty() # can only peak at a non empty stack
        return self.list[-1]

    def push(self, item):
        self.list.append(item)

    def pop(self):
        assert not self.isEmpty()
        return self.list.pop()


class StackLinked:
    """ a stack implemented using a linked list"""
    def __init__(self):
        self.head = None # a pointer to the head of the linked list
        self.size = 0

    def isEmpty(self):
        return self.size != 0

    def peek(self):
        assert not self.isEmpty()
        return self.head.data

    def pop(self):
        assert not self.isEmpty()
        pointer = self.head
        self.head = self.head.next
        return pointer

    def push(self, item):
        new_node = Linked(data=item)
        new_node.next = self.head
        self.head = new_node


""" using stack to solve balanced delimeter problem """
def stack_solution(word: str):
    stack_dict = {")":"(","}":"{","]":"["}
    stack = []
    for s in word:
        if s == '(' or s == '{' or s == '[':
            stack.append(s)
        # returns false if the stack is empty or the last element of the list isn't the same as the correspoding
        # dictionary value
        elif len(stack) == 0 or stack.pop() != stack_dict[i]:
            return False
        return True

def factorial(n):
    """ Using recursion """
    assert n >= 0 # must not be a negative integer
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonnaci(n):
    assert n >= 1
    if n == 1:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

def reverse_linked_list(n: Linked):
    """ print the data in a linked list using recursion"""
    head = n
    while head.data is not None:
        reverse_linked_list(head.next)
        print(head.data)


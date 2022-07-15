"""
Given the head of a sorted linked list,delete all duplicates such
that each element appears only once. Return the linked list sorted as well.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head

        # using two external reference to traverse the nodes
        prenode = head
        curnode = head.next
        while curnode is not None:
            if prenode.val == curnode.val:
                curnode = curnode.next
                prenode.next = curnode
            else:
                prenode = curnode
                curnode = curnode.next
        return head


"""Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by 
continuously following the next pointer. Internally, pos is used to denote the index of the node 
that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false."""


class _Solution:
    def hasCycle(self, head):
        if head is None:
            return False

        x = []
        while head is not None:
            if head.next in x:
                return True
            else:
                x.append(head)
                head = head.next
        return False


"""merge two sorted linked list given the heads"""


def mergesorted(head1, head2):
    dummynode = ListNode()
    current = dummynode
    pointer1, pointer2 = head1, head2
    while pointer1 and pointer2:  # iterate until one of the pointers point to null
        if pointer1.val < pointer2.val:
            current.next = pointer2
            pointer1 = pointer1.next
        else:
            current.next = pointer1
            pointer2 = pointer2.next
        current = current.next

    # set the current next parameter to the leftover pointer still active
    if pointer1:
        current.next = pointer1
    if pointer2:
        current.next = pointer2


""" removes every occurence of a value from a linked list """


def remove_node(head: ListNode, val: int):
    # create a dummynode
    dummynode = ListNode()
    dummynode.next = head

    # use two external reference
    prev = dummynode
    current = head

    # iterate until the current points to null
    while current:
        if current.val == val:
            prev.next = current.next
        else:
            prev = current
        current = current.next
    return dummynode.next  # returns the new linked list without returning the dummynode


def remove_middle_node(head: ListNode):
    # create a dummy node
    dummynode = ListNode(next=head)
    fast, slow = dummynode
    # this is called floyd cycle finding algorithm

    while fast and fast.next and fast.next.next:
        fast = fast.next
        slow = slow.next

    # at this point, the slow should be right in front of the middle node
    slow.next = slow.next.next
    return dummynode.next

def remove_all_node(head):
    pointer = head
    while pointer:
        pointer.data = None
        pointer = pointer.next
    return pointer is None


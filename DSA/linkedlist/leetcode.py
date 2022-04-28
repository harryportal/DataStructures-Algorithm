"""
Given the head of a sorted linked list,delete all duplicates such
that each element appears only once. Return the linked list sorted as well.

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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

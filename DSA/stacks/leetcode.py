"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        stack_dict = {')': "(", "}": "{", "]": "["}

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if len(stack) == 0 or stack_dict[i] != stack.pop():
                    return False
        return len(stack) == 0





""" Design a stack that supports push, pop, top, and retrieving
the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack. """

class MinStack:

    def __init__(self):
        self.stack = list()
        self.min = list()

    def push(self, val: int) -> None:
        if not self.min or val <= self.min[-1]:
            self.min.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        pop = self.stack.pop()
        if self.min and self.min[-1] == pop:
            self.min.pop()
        return pop

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
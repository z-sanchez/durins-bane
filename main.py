"""
Time complexity: 
O(n) traverse the list a couple times, but only as long as the list is


Space complexity: 
O(n) create a map depending on size of list

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        pointer = head

        while pointer:
            oldToCopy[pointer] = Node(pointer.val)
            pointer = pointer.next

        pointer = head

        while pointer:
            copy = oldToCopy[pointer]
            copy.next = oldToCopy[pointer.next]
            copy.random = oldToCopy[pointer.random]

        return oldToCopy[head]

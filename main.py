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

        curr = head

        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            newNode = oldToCopy[curr]
            newNode.next = oldToCopy[curr.next]
            newNode.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]

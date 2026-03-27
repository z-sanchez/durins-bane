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

        cursor = head

        while cursor:
            newNode = Node(cursor.val)
            oldToCopy[cursor] = newNode
            cursor = cursor.next

        cursor = head

        while cursor:
            newNode = oldToCopy[cursor]
            newNode.next = oldToCopy[cursor.next]
            newNode.random = oldToCopy[cursor.random]
            cursor = cursor.next

        return oldToCopy[head]

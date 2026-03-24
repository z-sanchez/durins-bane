
# Time Complexity: O(n), iterates through linked list no more than once
# Space Complexity: O(1), not creating anything except dummy, 1 every time

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create dummy node that points to list, we will return dummy.next (start of list)
        dummy = ListNode(0, head)

        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next

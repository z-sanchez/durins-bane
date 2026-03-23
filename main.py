# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# [2 -> 4 -> 6 -> 8]

# Time Complexity: O(n), iterate through list a few times but still linear
# Space Complexity: O(1), no new space created

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        right = head
        left = dummyNode

        while n > 0:
            right = right.next
            n -= 1
        # now that the pointers are spaced out, we advance them until we hit the end of the list
        while right:
            left = left.next
            right = right.next

        # making the adjustment to remove the node
        left.next = left.next.next

        # return from dummy, (head could have possibly been destroyed so it's safer to do this)
        return dummyNode.next

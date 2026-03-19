
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

        # advance right so that the distance between it and left are n + 1
        # Note about (n+1): because left is at the created dummy, it is actually one before the node that is n distance from right
        # this is done so that we are able to modify the prev node and skip over the nth we wish to remove
        while n > 0 and right:
            right = right.next
            n -= 1

        # now that the pointers are spaced out, we advance them until we hit the end of the list
        while right:
            left = left.next
            right = right.next

        # making the adjustment to remove the node
        left.next = left.next.next

        # return from dummy, (head could have possibly been destroyed so it's safer to do this)
        return dummy.next

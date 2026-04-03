# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# [2 -> 4 -> 6 -> 8]

# Time Complexity: O(n), iterate through list a few times but still linear
# Space Complexity: O(1), no new space created

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find midpoint
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        second = slow.next
        slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

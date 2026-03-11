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
        # slow will track where the midpoint falls
        # fast will tell is when we hit the end of list
        slow, fast = head, head.next

        while fast and fast.next:
            # shift slow forward
            slow = slow.next
            # continue to next node
            fast = fast.next.next

        # now slow points to the start of the second half, let's reverse it

        # use this to track the second half's start (it will be reversed by the time we're done)
        second = slow.next

        # need to track the previous node so we can adjust pointers
        prev = None

        # the first will become the last, so point next to null
        slow.next = None

        # will stop when we reach the final node in the original list
        while second:
            # hold whatever our node is pointing to
            temp = second.next
            # node will now point to whatever was before
            second.next = prev
            # update prev to this current node so the next loop can reference it
            prev = second
            # advance the point to the next node of the original list
            second = temp

        first = head
        # first node of the reversed list
        second = prev

        # traverse through second half and splice between original list nodes
        while second:
            # next placement in first list
            temp1 = first.next
            # next placement in reversed list
            temp2 = second.next

            # point connect the nodes
            first.next = second
            second.next = temp1

            # now we do the same but shift our pointers to the next positions
            first = temp1
            second = temp2

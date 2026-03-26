# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create dummy node
        dummy = ListNode()

        # start pointing to dummy
        cursor = dummy

        # this will hold carry over from adding
        carry = 0

        # may be left over carry to append to end of list (first number in total)
        while l1 or l2 or carry:
            # convert possible nones to 0s
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            # pull remainder into carry
            carry = total // 10

            # discard remainder, store whats left in new node
            newNode = ListNode(total % 10)

            # add to list
            cursor.next = newNode

            # move list pointers if next exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            # move cursor to new node
            cursor = cursor.next

        # return the new list
        return dummy.next

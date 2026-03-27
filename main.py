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

        while l1 or l2 or carry:
            valueOne = l1.val if l1 else 0
            valueTwo = l2.val if l2 else 0

            summed = valueOne + valueTwo + carry
            carry = summed // 10
            newNode = ListNode(summed % 10)
            cursor.next = newNode

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cursor = cursor.next

        # return the new list
        return dummy.next

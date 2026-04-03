# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2:
            l1_val = 0
            l2_val = 0
            if l1:
                l1_val = l1.val
            if l2:
                l2_val = l2.val

            total = l1_val + l2_val + carry
            carry = total // 10

            curr.next = ListNode(val = total % 10, next = None)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry == 1:
            curr.next = ListNode(val = 1, next = None)
        return dummy.next
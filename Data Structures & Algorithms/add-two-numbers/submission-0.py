# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next

        num2 = ""
        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        # reverse strings
        num1_reverse = ""
        i = len(num1) - 1
        while i >= 0:
            num1_reverse += num1[i]
            i -= 1

        num2_reverse = ""
        i = len(num2) - 1
        while i >= 0:
            num2_reverse += num2[i]
            i -= 1

        added = int(num1_reverse) + int(num2_reverse)
        added_str = str(added)
        added_reverse = ""
        i = len(added_str) - 1
        while i >= 0:
            added_reverse += added_str[i]
            i -= 1

        head = ListNode()
        curr = head
        for c in added_reverse:
            curr.next = ListNode(val = int(c), next = None)
            curr = curr.next

        return head.next

        


# [1, 2, 3]   [4, 5, 6]
# 321 + 654 = 975 --> [5, 7, 9]

# 
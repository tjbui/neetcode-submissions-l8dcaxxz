# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        if n > length:
            return head

        curr = head
        prev = None
        count = 0
        while count < (length - n):
            prev = curr
            curr = curr.next
            count += 1

        if prev:
            prev.next = curr.next
        else:
            temp = head.next
            head = None
            return temp

        return head


# [1,2,3,4], n = 2
# 1 -> 2 -> 3 -> 4

# 1 -> 2 -> 3 -> 4
#               curr
# Find length: len = 4

# len - n = 4 - 2 = 2
# 1 -> 2 -> 3 -> 4
# remove 2nd


# 1 -> 2 -> 3 -> 4 -> 5
# len = 5, n = 2
# remove 3rd


# [5]
# len = 1, n = 1
# 

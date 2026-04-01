# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head

        while curr:
            if not curr.next or not curr.next.next:
                break

            prev = None
            end = curr
            while end.next:
                prev = end
                end = end.next

            temp = curr.next
            curr.next = end
            end.next = temp

            if prev:
                prev.next = None
         
            curr = curr.next.next

        return

# [2, 4, 6, 8]
# 2 --> 4 --> 6 --> 8
# first iteration: curr = 2
#    2 --> 8
#    8 --> 4
#    6 --> None

# 2 --> 8 --> 4 --> 6
# second interation: curr = 4
# 

  

# 2 --> 4 --> 6 --> 8 --> 10
# first iteration:
#    2 --> 10
#    10 --> 4
#    8 --> None

# 2 --> 10 --> 4 --> 6 --> 8
# second iteration:
#    4 --> 8
#    8 --> 6
#    6 --> None

# 2 --> 10 --> 4 --> 8 --> 6
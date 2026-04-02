# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def rec(head, tail):
            if tail is None:
                return head
            
            head = rec(head, tail.next)
            if not head:
                return None
                
            if tail == head or head.next == tail:
                tail.next = None
                return None

            temp = head.next
            head.next = tail
            tail.next = temp

            return temp

        rec(head, head)
        return

# [2,4,6,8,10]
# recurse until tail
# rec(head, tail)

# 2 -> 4 -> 6 -> 8 -> 10
# rec(2, None)   return 2
# rec(2, 10) --> head = 2, tail = 10: return 4
# rec(2, 8)
# rec(2, 6)
# rec(2, 4)
# rec(2, 2)

# 2 --> 10 --> 4 --> 6 --> 8
# rec(2, 8) --> head 4, tail = 8: return 6
# rec(2, 6)
# rec(2, 4)
# rec(2, 2)

#                      <--
# 2 --> 10 --> 4 --> 8 --> 6 
# rec(2, 6) --> head = 6, tail = 6: return 6
# rec(2, 4)         
# rec(2, 2)

# 2 --> 10 --> 4 --> 8 --> 6
# rec(2, 4) --> head = 6, tail = 4
# rec(2, 2)



# 2 --> 4 --> 6 --> 8
# rec(2, 8) --> head = 2, tail = 8
# rec(2, 6)
# rec(2, 4)
# rec(2, 2)

# 2 --> 8 --> 4 --> 6 --> 8
# rec(2, 6) --> head = 4, tail = 6
# rec(2, 4)
# rec(2, 2)

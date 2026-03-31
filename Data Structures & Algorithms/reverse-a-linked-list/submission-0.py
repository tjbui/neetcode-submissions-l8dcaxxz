# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        cur_node = head
        next_node = cur_node.next

        cur_node.next = None

        while next_node is not None:
            temp = next_node.next
            next_node.next = cur_node

            cur_node = next_node
            next_node = temp

        return cur_node
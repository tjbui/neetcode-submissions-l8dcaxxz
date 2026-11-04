# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode = head
        prevNode = None

        while currNode:
            tempNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = tempNode

        return prevNode
        

#    0 -> 1 -> 2 -> 3
#    c
# p
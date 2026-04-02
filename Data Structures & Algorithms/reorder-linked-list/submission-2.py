# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # slow, fast ptr: O(n) time, O(1) space
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        if not head.next:
            return

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        tail = slow.next
        prev = None
        while tail:
            temp = tail.next
            tail.next = prev
            prev = tail
            tail = temp

        slow.next = None

        tail = prev # new tail
        while head:
            temp_head = head.next
            if tail:
                temp_tail = tail.next
                tail.next = temp_head
            head.next = tail
            head = temp_head
            tail = temp_tail

        return





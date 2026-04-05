# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return None

        return self.mergek(lists)

    def mergek(self, list_of_heads):
        if len(list_of_heads) == 1:
            return list_of_heads[0]

        m = len(list_of_heads) // 2
        left_head = self.mergek(list_of_heads[: m])
        right_head = self.mergek(list_of_heads[m:])

        return self.merge2(left_head, right_head)

    def merge2(self, head_1, head_2):
        dummy = ListNode()

        curr = dummy
        while head_1 and head_2:
            if head_1.val < head_2.val:
                curr.next = head_1
                head_1 = head_1.next
                curr = curr.next
            else:
                curr.next = head_2
                head_2 = head_2.next
                curr = curr.next

        while head_1:
            curr.next = head_1
            head_1 = head_1.next
            curr = curr.next
        while head_2:
            curr.next = head_2
            head_2 = head_2.next
            curr = curr.next

        return dummy.next


# 1 --> 2 --> 4     1 --> 3 --> 5    3 --> 6    4    7 --> 9

# 1 --> 2 --> 4     1 --> 3 --> 5
#   1 --> 2 --> 3 --> 4 --> 5

# 1 --> 2 --> 3 --> 4 --> 5          3 --> 6
#   1 --> 2 --> 3 --> 3 --> 4 --> 5 --> 6 
# O(n^2)


# [1 --> 2 --> 4,   1 --> 3 --> 5,   3 --> 6,   4,   7 --> 9]
# [1 --> 2 --> 4,   1 --> 3 --> 5,   3 --> 6]   [4,   7 --> 9]

# [1 --> 2 --> 4,   1 --> 3 --> 5]    [3 --> 6]   [4]    [7 --> 9]

# [1 --> 2 --> 4]   [1 --> 3 --> 5]   [3 --> 6]   [4]   [7 --> 9]
# 

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        m = {}

        curr = head
        while curr:
            m[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.random:
                m[curr].random = m[curr.random]
            else:
                m[curr].random = None
            
            if curr.next:
                m[curr].next = m[curr.next]
            else:
                m[curr].next = None

            curr = curr.next

        return m[head]
        

# 3 -> 7 -> 4 -> 5 -> null
# 3 -r-> null
# 7 -r-> 5
# 4 -r-> 3
# 5 -r-> 7

# 
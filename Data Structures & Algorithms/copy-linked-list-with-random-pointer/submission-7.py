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
        origToCopy = {}
        origToCopy[None] = None

        currNode = head      
        while currNode:
            newNode = Node(currNode.val)
            origToCopy[currNode] = newNode

            currNode = currNode.next

        currNode = head
        while (currNode):
            copyNode = origToCopy[currNode]
            copyNode.random = origToCopy[currNode.random]
            copyNode.next = origToCopy[currNode.next]
            currNode = currNode.next

        return origToCopy[head]


#       -------->
# 3 -> 7 -> 4 -> 5 -> null
#  ------------------>
#  <--------
#       <---------

# 
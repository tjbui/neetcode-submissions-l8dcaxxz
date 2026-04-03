from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        ret = []

        q.append(root)
        while q:
            qLen = len(q)
            temp = []

            for i in range(qLen):
                curr = q.popleft()
                temp.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ret.append(temp)

        return ret
# [1]

# [2, 3] --> [2, 3, 4, 5, 6, 7]

# [4, 5, 6, 7]
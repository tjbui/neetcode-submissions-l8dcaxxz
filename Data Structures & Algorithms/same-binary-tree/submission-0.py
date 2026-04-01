# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkSame(root_p, root_q):
            if root_p is None and root_q:
                return False
            if root_q is None and root_p:
                return False
            if root_q is None and root_p is None:
                return True

            if root_q.val != root_p.val:
                return False
            
            return (checkSame(root_p.left, root_q.left) and
                    checkSame(root_p.right, root_q.right))

        return checkSame(p, q)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_val = 1000
        min_val = -1000

        return self.checkValid(root, min_val, max_val)


    def checkValid(self, root: TreeNode, min_val: int, max_val: int) -> bool:
        if root is None:
            return True

        if root.val < min_val or root.val > max_val:
            return False

        return (self.checkValid(root.left, min_val, root.val - 1) and
               self.checkValid(root.right, root.val + 1, max_val))
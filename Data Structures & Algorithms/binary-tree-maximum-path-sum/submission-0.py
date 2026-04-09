# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float("-infinity")
        def dfs(node):
            nonlocal best

            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            best = max(best, left + node.val + right)

            return max(left + node.val, right + node.val, node.val)
        
        dfs(root)
        return best
        

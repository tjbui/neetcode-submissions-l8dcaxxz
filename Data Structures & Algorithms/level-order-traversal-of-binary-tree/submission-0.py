# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # tj original solution
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def get_height(root):
            if root is None:
                return 0
            
            left = get_height(root.left)
            right = get_height(root.right)

            return 1 + max(left, right)
        height = get_height(root)

        out = [[] for _ in range(height)]

        def traverse(root, level):
            if root is None:
                return
            
            out[level].append(root.val)
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)
            return

        traverse(root, 0)
        return out
# 
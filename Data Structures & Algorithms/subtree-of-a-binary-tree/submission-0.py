# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isSameTree(self, root_x, root_y):
        if root_x is None and root_y is None:
            return True
        if root_x is None or root_y is None:
            return False
        
        if root_x.val != root_y.val:
            return False

        return (self.isSameTree(root_x.left, root_y.left) and 
                self.isSameTree(root_x.right, root_y.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (self.isSameTree(root, subRoot)):
            return True
        if not root:
            return False
        
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
    
    



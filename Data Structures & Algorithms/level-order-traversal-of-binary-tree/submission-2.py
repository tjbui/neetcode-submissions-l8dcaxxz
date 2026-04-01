from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # classic BFS approach
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        out = []

        q = deque()
        q.append(root)

        while q:
            qLen = len(q)

            temp_list = []
            for _ in range(qLen):
                curr_node = q.popleft()
                temp_list.append(curr_node.val)

                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            
            out.append(temp_list)

        return out



        

# queue: [1]
# queue: [1] popleft() 
# queue: []     ---> append temp_list
# 
# queue: [2, 3]
#        [3]    ---> temp_list = 

        

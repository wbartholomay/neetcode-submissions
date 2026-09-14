# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if abs(left_height - right_height) > 1 or left_height == -1 or right_height == -1:
                return -1

            return max(left_height, right_height) + 1
        
        res = dfs(root)
        if res == -1:
            return False
        
        return True
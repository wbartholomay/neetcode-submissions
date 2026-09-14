from typing import Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, min_val, max_val):
            if not node:
                return True
            if not(min_val < node.val < max_val):
                return False
            
            if not valid(node.left, min_val, node.val) or not valid(node.right, node.val, max_val):
                return False
            
            return True
        return valid(root, -float('inf'), float('inf'))
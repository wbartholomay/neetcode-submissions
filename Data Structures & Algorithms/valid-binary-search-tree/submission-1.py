from typing import Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[TreeNode]) -> Tuple[bool, Optional[int], Optional[int]]:
            if node is None:
                return True, None, None
            
            is_left_child_valid, left_min, left_max = dfs(node.left)
            is_right_child_valid, right_min, right_max = dfs(node.right)

            # print(f"Val: {node.val}, left max: {left_max}, left min: {left_min}, right min: {right_min}, right_max: {right_max}")

            if not is_left_child_valid or not is_right_child_valid:
                return False, 0, 0

            # print(f"Val: {node.val}, right_min: {right_min}, condition: {node.val >= right_min}")
            if (left_max is not None and node.val <= left_max) or (right_min is not None and node.val >= right_min):
                return False, 0, 0

            tree_max = max(v for v in [left_max, right_max, node.val] if v is not None)
            tree_min = min(v for v in [left_min, right_min, node.val] if v is not None)

            return True, tree_min, tree_max
        
        is_valid_tree, _, _ = dfs(root)
        return is_valid_tree

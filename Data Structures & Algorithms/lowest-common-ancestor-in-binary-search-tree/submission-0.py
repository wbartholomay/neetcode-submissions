from typing import Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None

        def dfs(node: Optional[TreeNode]) -> Tuple[bool, bool]:
            nonlocal res
            if node is None:
                return False, False
            
            left_p, left_q = dfs(node.left)
            right_p, right_q = dfs(node.right)

            found_p = left_p or right_p or node == p
            found_q = left_q or right_q or node == q
            # print(f"Node val: {node.val}, found p: {found_p}, found q: {found_q}")

            if found_p and found_q and res is None:
                res = node

            return found_p, found_q
        dfs(root)

        return res
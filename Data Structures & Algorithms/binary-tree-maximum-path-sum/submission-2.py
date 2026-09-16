# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')
        def dfs(node):
            nonlocal res
            left_max, right_max = 0, 0
            if node.left:
                left_max = max(left_max, dfs(node.left))
            if node.right:
                right_max = max(right_max, dfs(node.right))

            res = max(res, node.val + left_max + right_max)

            return node.val + max(left_max, right_max)
        dfs(root)
        return res

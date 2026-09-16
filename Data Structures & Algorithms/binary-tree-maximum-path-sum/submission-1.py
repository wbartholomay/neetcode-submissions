# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')
        def dfs(root):
            nonlocal res
            if root is None:
                return 0
            left_max = dfs(root.left)
            right_max = dfs(root.right)

            res = max(res, root.val + left_max + right_max, root.val + left_max, root.val + right_max, root.val)

            if left_max < 0 and right_max < 0:
                return root.val

            return root.val + max(left_max, right_max)
        
        dfs(root)
        return res
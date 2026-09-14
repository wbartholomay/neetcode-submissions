# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = []
        depth = 1
        queue.append((root, 1))

        while queue:
            node, node_depth = queue.pop()
            if node.left:
                queue.append((node.left, node_depth + 1))
            if node.right:
                queue.append((node.right, node_depth + 1))
            depth = max(depth, node_depth)
        return depth
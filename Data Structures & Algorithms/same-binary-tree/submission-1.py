# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        def dfs(node_p: Optional[TreeNode], node_q: Optional[TreeNode]) -> bool:
            if node_p is None and node_q is None:
                return True
            elif node_p is None or node_q is None:
                return False
            elif node_p.val != node_q.val:
                return False
            
            if not dfs(node_p.left, node_q.left):
                return False
            
            if not dfs(node_p.right, node_q.right):
                return False
            
            return True
        
        return dfs(p, q)
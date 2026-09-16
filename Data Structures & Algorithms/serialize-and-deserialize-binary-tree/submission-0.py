# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        if root is None:
            return res

        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                res += "N,"
                continue

            stack.append(node.right)
            stack.append(node.left)
            res += str(node.val)
            res += ","
        
        return res[:-1]

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        i = 0
        vals = data.split(",")

        def dfs():
            nonlocal i
            if vals[i] == "N":
                i += 1
                return None
            node = TreeNode(int(vals[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
        
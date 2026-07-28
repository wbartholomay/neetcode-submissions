"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        new_root = Node(node.val)
        nodes = {node.val : new_root}

        def dfs(old_node, new_node):
            for neighbor in old_node.neighbors:
                if nodes.get(neighbor.val) is not None:
                    new_node.neighbors.append(nodes[neighbor.val])
                else:
                    new_neighbor = Node(neighbor.val)
                    nodes[neighbor.val] = new_neighbor
                    dfs(neighbor, new_neighbor)
                    new_node.neighbors.append(new_neighbor)
                

        dfs(node, new_root)
        return new_root
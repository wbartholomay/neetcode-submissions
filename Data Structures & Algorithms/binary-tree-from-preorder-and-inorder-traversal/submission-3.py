# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indexes = {}
        for i in range(len(inorder)):
            inorder_indexes[inorder[i]] = i

        def buildTreeHelper(pre_start, pre_end, in_start, in_end):
            if pre_end < pre_start:
                return None

            root = TreeNode(preorder[pre_start])
            inorder_arr_root_index = inorder_indexes[root.val]
            left_size = inorder_arr_root_index - in_start

            root.left = buildTreeHelper(pre_start + 1, pre_start + left_size, in_start, inorder_arr_root_index)
            root.right = buildTreeHelper(pre_start + left_size + 1, pre_end, inorder_arr_root_index + 1, in_end)
            
            return root
        
        return buildTreeHelper(0, len(preorder) - 1, 0, len(inorder) - 1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        # Since leaf nodes are in a left-to-right sequence, consider Preorder traversal
        def preorder_traversal(node, leaf_sequence):
            if not node:
                return leaf_sequence
            if not node.left and not node.right:
                # leaf node
                leaf_sequence.append(node.val)
            preorder_traversal(node.left, leaf_sequence)
            preorder_traversal(node.right, leaf_sequence)
        
        leaf_seq_1 = []
        leaf_seq_2 = []
        preorder_traversal(root1, leaf_seq_1)
        preorder_traversal(root2, leaf_seq_2)

        return leaf_seq_1 == leaf_seq_2

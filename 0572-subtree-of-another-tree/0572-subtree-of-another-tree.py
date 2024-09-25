# Time Complexity: O(N^2)
# Space Complexity: O(N^2)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.is_subtree_recursive(root, subRoot)

    def is_subtree_recursive(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if self.is_same_tree(root, subRoot):
            return True
        return self.is_subtree_recursive(root.left, subRoot) or self.is_subtree_recursive(root.right, subRoot)
    
    def is_same_tree(self, node1, node2):
        if not node1 and not node2: # Both are leaf nodes
            return True
        if not node1 or not node2: # Only 1 of them is leaf node
            return False
        if node1.val != node2.val:
            return False
        return self.is_same_tree(node1.left, node2.left) and self.is_same_tree(node1.right, node2.right)

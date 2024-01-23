# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check for leaf nodes
        if not p and not q:
            return True
        # Check if one of them is a leaf node and the other is not. Also check if the values are different
        if not p or not q or p.val != q.val:
            return False
        # Check both the left and right sub-tree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


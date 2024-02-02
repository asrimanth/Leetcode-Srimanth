# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traversal(a,b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            return a.val == b.val and traversal(a.left, b.right) and traversal(a.right, b.left)
        return traversal(root.left,root.right)
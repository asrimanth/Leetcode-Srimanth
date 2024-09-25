# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self.result = True
        def recursive(node):
            left_depth = recursive(node.left) if node.left else 0
            right_depth = recursive(node.right) if node.right else 0

            if abs(left_depth - right_depth) > 1:
                self.result = False
                return -1
            return max(left_depth, right_depth) + 1
        result = recursive(root)
        return self.result

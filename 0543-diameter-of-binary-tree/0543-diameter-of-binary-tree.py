# Time Complexity: O(N)
# Space Complexity: O(H), H = height for balanced tree, O(N) if not balanced.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def recursive(node):
            left_height = recursive(node.left) if node.left else 0
            right_height = recursive(node.right) if node.right else 0
            self.max_diameter = max(left_height + right_height, self.max_diameter)
            return 1 + max(left_height, right_height)
        recursive(root)
        return self.max_diameter

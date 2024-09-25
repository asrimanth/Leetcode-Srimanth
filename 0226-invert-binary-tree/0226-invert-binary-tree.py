# Time Complexity: O(N)
# Space Complexity: O(N) # Recursion internally uses a stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        if root is None:
            return root
        def recursive(node):
            if node is None:
                return
            node.left, node.right = node.right, node.left
            recursive(node.left)
            recursive(node.right)
        recursive(node)
        return root

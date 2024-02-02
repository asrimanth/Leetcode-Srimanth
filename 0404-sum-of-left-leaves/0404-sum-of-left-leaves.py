# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left):
            if node is None:
                return 0
            if node.left is None and node.right is None and is_left:
                # leaf node
                return node.val
            return dfs(node.left, True) + dfs(node.right, False)

        left_sum = dfs(root, False)
        return left_sum
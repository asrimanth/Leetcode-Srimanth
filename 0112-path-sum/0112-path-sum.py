# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # DFS
        stack = [(root, root.val)]
        while len(stack) != 0:
            curr, curr_sum = stack.pop()
            
            if curr.left is not None:
                stack.append((curr.left, curr_sum+curr.left.val))
            if curr.right is not None:
                stack.append((curr.right, curr_sum+curr.right.val))
            
            if curr.left is None and curr.right is None and curr_sum == targetSum:
                return True
        return False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        fringe = deque([(root, 1)])
        max_depth = -99999
        while len(fringe) != 0:
            curr, depth = fringe.popleft() # BFS
            if curr.left is None and curr.right is None:
                max_depth = max(depth, max_depth)
            if curr.left is not None:
                fringe.append((curr.left, depth+1))
            if curr.right is not None:
                fringe.append((curr.right, depth+1))
        return max_depth
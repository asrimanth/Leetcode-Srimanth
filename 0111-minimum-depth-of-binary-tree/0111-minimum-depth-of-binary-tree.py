# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        fringe = deque([(root, 1)])
        min_depth = 9999
        if root is None:
            return 0

        while len(fringe) != 0:
            curr, depth = fringe.popleft() #BFS
            # curr, depth = fringe.pop() # DFS
            if curr.left is None and curr.right is None:
                min_depth = min(depth, min_depth)
            if curr.left is not None:
                fringe.append((curr.left, depth+1))
            if curr.right is not None:
                fringe.append((curr.right, depth+1))
        return min_depth
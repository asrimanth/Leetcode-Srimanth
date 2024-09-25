# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        # BFS
        fringe = [(root, root.val)]
        num_good_nodes = 0
        while len(fringe):
            for _ in range(len(fringe)):
                curr, max_so_far = fringe.pop()
                if curr.val >= max_so_far:
                    num_good_nodes += 1
                if curr.left is not None:
                    max_so_far = max(max_so_far, curr.val)
                    fringe.append([curr.left, max_so_far])
                if curr.right is not None:
                    max_so_far = max(max_so_far, curr.val)
                    fringe.append([curr.right, max_so_far])
        return num_good_nodes

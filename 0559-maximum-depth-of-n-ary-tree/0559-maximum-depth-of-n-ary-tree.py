"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_depth = 1
        if root is None or len(root)==0 :
            return 0
        fringe = deque([(max_depth, root)])
        while len(fringe) != 0:
            x = fringe.popleft()
            curr_depth, curr_node = x
            print(curr_depth, curr_node.val)
            if max_depth < curr_depth:
                max_depth = curr_depth
            fringe.extend([(curr_depth+1, child) for child in curr_node.children])
        return max_depth

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        fringe = deque([(0, root)])
        prev_level, prev_node = -1, None
        while fringe:
            curr_level, curr_node = fringe.popleft()
            if prev_level == curr_level:
                prev_node.next = curr_node
                prev_node = curr_node
            else:
                prev_level, prev_node = curr_level, curr_node
            if curr_node.left is not None:
                fringe.append((curr_level+1, curr_node.left))
                fringe.append((curr_level+1, curr_node.right))
        return root
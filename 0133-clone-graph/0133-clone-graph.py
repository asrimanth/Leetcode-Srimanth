"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hashmap = dict()
        hashmap[node.val] = Node(node.val)
        # BFS
        fringe = deque([node])
        while len(fringe):
            curr = fringe.popleft()
            for nei in curr.neighbors:
                if nei.val not in hashmap:
                    hashmap[nei.val] = Node(nei.val)
                    fringe.append(nei)
                hashmap[curr.val].neighbors.append(hashmap[nei.val])
        return hashmap[node.val]

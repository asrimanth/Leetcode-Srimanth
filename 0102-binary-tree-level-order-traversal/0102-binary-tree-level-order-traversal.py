# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

# Time complexity: BFS is O(n).
# Space complexity: O(m), where m is the max number of nodes at a given level.
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        fringe = deque([root])
        result = []
        while len(fringe) > 0:
            result.append([node.val for node in fringe])
            fringe = [child for node in fringe for child in (node.left, node.right) if child]
        return result



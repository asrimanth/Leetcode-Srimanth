# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Perform level order traversal using BFS
        # Update the rightmost node for each level
        if not root:
            return []
        fringe = deque([(root, 0)])
        result = defaultdict(int)
        while len(fringe):
            for _ in range(len(fringe)):
                curr, curr_level = fringe.popleft()
                if curr.left:
                    fringe.append((curr.left, curr_level+1))
                if curr.right:
                    fringe.append((curr.right, curr_level+1))
            result[curr_level] = curr.val
        return list(result.values())

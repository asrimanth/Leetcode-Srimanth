# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        if not root or root is None:
            return []
        fringe = deque([(root)])
        result = []
        while fringe:
            level = []
            for _ in range(len(fringe)):
                root = fringe.popleft()
                if root.left:
                    fringe.append(root.left)
                if root.right:
                    fringe.append(root.right)
                level.append(root.val)
            result.append(level)
        return result[::-1]
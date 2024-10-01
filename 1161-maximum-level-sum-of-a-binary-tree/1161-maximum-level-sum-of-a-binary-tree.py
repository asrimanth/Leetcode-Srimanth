# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # BFS
        fringe = deque([(root, 1)])
        level_sums = defaultdict(int)

        while fringe:
            curr_node, curr_level = fringe.popleft()
            level_sums[curr_level] += curr_node.val
            # Should be strictly less than
            # Since we need the smallest level x, the sum of values of nodes at level x is maximal.
            if curr_node.left is not None:
                fringe.append((curr_node.left, curr_level+1))
            if curr_node.right is not None:
                fringe.append((curr_node.right, curr_level+1))

        max_level, max_sum = -9999999, -99999999
        for level, val in level_sums.items():
            if max_sum < val:
                max_sum = val
                max_level = level
        return max_level

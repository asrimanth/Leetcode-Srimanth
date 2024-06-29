# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # BFS
        fringe = [(f"{root.val}", root)]
        result = []
        while fringe:
            current_path, current_node = fringe.pop()
            if current_node.left is not None:
                fringe.append((f"{current_path}->{current_node.left.val}", current_node.left))
            if current_node.right is not None:
                fringe.append((f"{current_path}->{current_node.right.val}", current_node.right))
            if current_node.left is None and current_node.right is None:
                result.append(current_path)
        return result

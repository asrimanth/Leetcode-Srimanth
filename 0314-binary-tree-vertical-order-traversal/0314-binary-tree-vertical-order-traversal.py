# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        fringe = deque([(0, root)])
        
        data = defaultdict(list)
        while len(fringe) > 0:
            curr_level, curr_node = fringe.popleft()
            if curr_node is not None:
                data[curr_level].append(curr_node.val)
                if curr_node.left is not None:
                    fringe.append((curr_level-1, curr_node.left))
                if curr_node.right is not None:
                    fringe.append((curr_level+1, curr_node.right))

        data = sorted(data.items())
        data = [item for _, item in data]
        return data
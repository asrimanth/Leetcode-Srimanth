# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity for FindElements: O(N), Find: O(1)
# Space Complexity: O(N)
from collections import deque
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.elements = set()
        self._recover_tree()

    def _recover_tree(self):
        # first tree traversal using BFS
        fringe = deque([(self.root, 0)])
        while fringe:
            curr, val = fringe.popleft()
            self.elements.add(val)
            if curr.left is not None:
                fringe.append((curr.left, ((2*val)+1)))
            if curr.right is not None:
                fringe.append((curr.right, ((2*val)+2)))

    def find(self, target: int) -> bool:
        return target in self.elements


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # result = []
        # def inorder_traversal(node):
        #     if not node:
        #         return
        #     inorder_traversal(node.left)
        #     result.append(node.val)
        #     inorder_traversal(node.right)

        self.count = 0
        self.kth_elem = -1
        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            self.count += 1
            if self.count == k: self.kth_elem = node.val
            inorder_traversal(node.right)
        inorder_traversal(root)
        return self.kth_elem

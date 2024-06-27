# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Preorder traversal using recursion
# Time Complexity: O(N), N being the number of nodes
# Space Complexity: O(N)
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        data = []
        def preorder(node):
            if node is not None:
                data.append(node.val)
                preorder(node.left)
                preorder(node.right)
            else:
                return
        preorder(root)
        return data

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Postorder traversal using recursion
# Time Complexity: O(N), N being the number of nodes
# Space Complexity: O(N)
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        data = []
        def postorder(node):
            if node is not None:
                postorder(node.left)
                postorder(node.right)
                data.append(node.val)
            else:
                return
        postorder(root)
        return data

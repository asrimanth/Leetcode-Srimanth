# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_ll = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = new_ll
            new_ll = current
            current = next_node
        return new_ll
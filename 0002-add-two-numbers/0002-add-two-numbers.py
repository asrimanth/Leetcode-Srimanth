# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = ListNode()
        out = result
        while l1 or l2:
            if l1: out.val += l1.val
            if l2: out.val += l2.val
            carry = out.val // 10
            out.val = out.val % 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if (carry != 0) or l1 or l2:
                out.next = ListNode(carry)
                out = out.next

        return result
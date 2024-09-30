# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time Complexity: O(N)
# Space Complexity: O(2*N) = O(N)
from copy import deepcopy
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        rev = self.reverse(deepcopy(head))
        max_sum = -1
        while head:
            max_sum = max(head.val + rev.val, max_sum)
            head = head.next
            rev = rev.next
        return max_sum

    def reverse(self, node):
        # 1 -> 2 -> 3 -> 4
        prev, curr = None, node
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

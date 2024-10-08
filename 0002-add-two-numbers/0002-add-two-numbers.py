# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        out = result
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + carry

            # New digit and carry
            carry = val // 10
            val %= 10 # Units place only
            out.next = ListNode(val)

            # Update pointers
            out = out.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # After all adds, put carry in the final place.
        if carry != 0:
            out.next = ListNode(carry)
            out = out.next
        return result.next

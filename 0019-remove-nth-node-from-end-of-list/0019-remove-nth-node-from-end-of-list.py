# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Move right pointer to the nth node from left
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # Now, move left until right is None
        # This makes sure that left is at the n-1th node from end
        while right:
            left = left.next
            right = right.next
        
        # Now left is at the n-1th node from the end of list
        left.next = left.next.next
        # 1 -> 2 -> 3 = 1 -> 3

        return dummy.next

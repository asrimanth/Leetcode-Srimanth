# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 1
        tail = head

        while tail.next:
            length += 1
            tail = tail.next
        
        # k = k if k < length else k % length
        k = k % length

        # Make the list circular
        tail.next = head

        # Find the breakpoint from the start
        temp = head
        for i in range(length - k - 1):
            temp = temp.next
        answer = temp.next
        temp.next = None # Break the circular list into singly linked list.

        return answer

# Time Complexity: O(N/2) + O(N/2) + O(N) = O(N)
# Space Complexity: O(1)
# https://www.youtube.com/watch?v=S5bfdUTrKLM

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Step 1: Find the midpoint of the list using slow and fast pointers
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Now slow is at the midpoint. 
        right_half = slow.next
        slow.next = None

        # Step 2: Reverse the right half
        prev, curr = None, right_half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # prev stores the reference to the reversed right half, curr is None
        # Step 3: The merging algo, alternatively place nodes from 1st and 2nd.
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse_list_iter(head)
    
    def reverse_list_iter(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach: Save node.next pointer in a temp
        # Then break node.next and assign it to previous node.
        # Hence, we reverse the connections as we move along.
        prev, curr = None, head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes_at_k = []
        temp = head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        nodes_at_k = []
        temp = head
        while count >= k:
            # reverse ll here
            reversed_left, right = self.reverse_ll(temp, k)
            nodes_at_k.append(reversed_left)
            temp = right
            count -= k
        last_piece = temp

        result = ListNode(-1)
        temp = result
        for idx in range(len(nodes_at_k)):
            temp.next = nodes_at_k[idx]
            for _ in range(k):
                temp = temp.next
        temp.next = last_piece
        return result.next

    def reverse_ll(self, node, k):
        prev, curr = None, node
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev, curr

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        result = Node(-1)
        dummy = result
        temp = head
        # 1st pass: Save a new list with only the next pointers
        # Also save the original:new nodes in a hashmap
        hash_map = {None:None}
        while temp:
            new_node = Node(temp.val, None, None)
            dummy.next = new_node
            # Save nodes in hash_map
            hash_map[temp] = new_node
            temp = temp.next
            dummy = dummy.next

        # 2nd pass: Copy the random connections
        temp = head
        dummy = result.next
        current_idx = 0
        while temp:
            dummy.random = hash_map[temp.random]
            temp = temp.next
            dummy = dummy.next

        return result.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not len(lists):
            return None
        elif len(lists) == 1:
            return lists[0]

        merged_node = lists[0]

        # Time Complexity: O(N * K)
        # Space Complexity: O(1) excluding result
        # Less optimized - merge current list with next list
        # for i in range(1, len(lists)):
        #     merged_node = self.merge(merged_node, lists[i])

        # Neetcode way
        # https://www.youtube.com/watch?v=q5a5OiGbT6Q
        i, j = 0, len(lists)-1
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                merged_lists.append(self.merge(list1, list2))
            lists = merged_lists
        return lists[0]


        return merged_node
    
    def merge(self, node1, node2):
        result = ListNode(0)
        temp = result
        while node1 and node2:
            val1 = node1.val if node1 else -999999999
            val2 = node2.val if node2 else -999999999
            if val1 <= val2:
                temp.next = ListNode(val1)
                node1 = node1.next
            else:
                temp.next = ListNode(val2)
                node2 = node2.next
            temp = temp.next
        if node1:
            temp.next = node1
        elif node2:
            temp.next = node2
        return result.next

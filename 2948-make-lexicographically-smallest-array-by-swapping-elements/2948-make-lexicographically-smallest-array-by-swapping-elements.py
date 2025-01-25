from collections import deque
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        """
        Overall, what we want is to group close elements, sort them, and put them back in their positions.
        Examples: 
        [3, 2, 5, 1]; limit = 1 -> [1, 2, 5, 3]
        [1, 7, 6, 18, 2, 1], limit = 3 -> [1, 6, 7, 81, 1, 2]
        Approach:
        1. Sort the initial array
        2. Create number-group mapping according to the limit. Numbers are unique
        3. Maintain a list of queues (list of groups).
        3. Loop through each group and place each element from the group to the position
        Full video: https://www.youtube.com/watch?v=-FGl6dzPexY
        """
        num_group_map = {}
        groups = []

        for num in sorted(nums):
            # abs(num - groups[-1][-1]) > limit
            # Groups are split using the above criteria. groups[-1][-1] is the prev latest num.
            # If the diff exceeds the limit, we create a new group.
            # Since our nums are sorted, our groups are also sorted.
            if not len(groups) or abs(num - groups[-1][-1]) > limit:
                groups.append(deque())
            groups[-1].append(num)
            num_group_map[num] = len(groups) - 1
        
        # Fill the result
        result = []
        for num in nums:
            group_idx = num_group_map[num]
            element = groups[group_idx].popleft()
            result.append(element)
        return result

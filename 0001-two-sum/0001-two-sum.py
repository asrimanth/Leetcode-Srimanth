# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map approach
        hash_map = dict()

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return (hash_map[complement], i)
            hash_map[num] = i
        return None

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_idx = 1
        size = len(nums)
        for i in range(1, size):
            # If the next number is a unique number:
            if nums[i] != nums[i-1]:
                nums[insert_idx] = nums[i]
                insert_idx += 1
        return insert_idx

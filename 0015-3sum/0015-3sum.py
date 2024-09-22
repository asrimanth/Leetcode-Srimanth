# Time Complexity: O(N*log(N)) + O(N^2) = O(N^2)
# Space Complexity: O(N)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Two pointers with hashmap
        # First sort the input array for the 2 pointer setup
        nums = sorted(nums)
        result = []
        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx-1]:
                # If same number in current and previous
                # Do NOT recompute the triplets.
                continue

            left, right = idx+1, len(nums)-1
            curr_target = -1 * num
            while left < right:
                if nums[left] + nums[right] > curr_target:
                    right -= 1
                elif nums[left] + nums[right] < curr_target:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return result

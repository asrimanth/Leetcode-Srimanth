# Time Complexity: O(2*log(n))
# Space Complexity: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, is_low):
            low, high = 0, len(nums)-1
            result_idx = -1
            while low <= high:
                mid = (low + high)//2
                if nums[mid] == target:
                    result_idx = mid
                    if is_low:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return result_idx
        
        low = binary_search(nums, target, True)
        high = binary_search(nums, target, False)

        return [low, high]

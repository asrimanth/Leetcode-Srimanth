# Time Complexity: O(N^2)
# Space Complexity: O(1)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        result = 0
        diff = 9999999999
        n = len(nums)
        for i in range(n):
            left, right = i+1, n-1
            while left < right:
                num1, num2, num3 = nums[i], nums[left], nums[right]
                total = num1 + num2 + num3
                # Two pointers
                if total > target:
                    right -= 1
                else:
                    left += 1
                # Update diff and result
                if abs(total - target) < diff:
                    diff = abs(total - target)
                    result = total
                # print(num1, num2, num3, total, target, diff, result)
        return result

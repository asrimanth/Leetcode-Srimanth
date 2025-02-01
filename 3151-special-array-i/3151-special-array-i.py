class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        for i in range(1, len(nums)):
            prev, curr= nums[i-1], nums[i]
            if prev%2 == curr%2:
                return False
        return True

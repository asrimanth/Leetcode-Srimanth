class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Backtracking
        if len(nums) == 1:
            return [nums]
        nums = sorted(nums)
        n = len(nums)
        result = set()
        def dfs(idx):
            if idx == n-1:
                result.add(tuple(nums))
                return
            for j in range(idx, n):
                nums[idx], nums[j] = nums[j], nums[idx]
                dfs(idx+1)
                # backtrack
                nums[idx], nums[j] = nums[j], nums[idx]
        dfs(0)
        return result

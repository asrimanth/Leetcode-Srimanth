
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        # Backtracking
        n = len(nums)
        result = set()
        def dfs(i):
            if i == n:
                return
            for j in range(i+1, n):
                nums[i], nums[j] = nums[j], nums[i]
                result.add(tuple(nums.copy()))
                dfs(i+1)
                # Backtrack => swap to original
                nums[i], nums[j] = nums[j], nums[i]
                result.add(tuple(nums.copy()))
                dfs(i+1)
        dfs(0)
        return list(result)
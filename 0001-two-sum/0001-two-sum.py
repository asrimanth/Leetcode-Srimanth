class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.hashmap_solution(nums, target)
    
    def hashmap_solution(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        n = len(nums)
        hashmap = dict() # num:index is the mapping.
        for i in range(n):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        return None

    def brute_force_solution(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity: O(N ** 2)
        # Space Complexity: O(1)
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

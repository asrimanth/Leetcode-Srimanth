# Time Complexity: O(2*N) = O(N)
# Space Complexity: O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        prefix_prod = 1
        suffix_prod = 1
        for i in range(n):
            # loop for prefix product
            result[i] = prefix_prod
            prefix_prod *= nums[i]
        
        for i in range(n-1, -1, -1):
            # loop for suffix prod
            result[i] *= suffix_prod
            suffix_prod *= nums[i]
        return result

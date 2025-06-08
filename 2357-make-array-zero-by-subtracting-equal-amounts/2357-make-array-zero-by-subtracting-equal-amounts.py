# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Number of unique non-zero elements in nums
        hashset = set()
        for num in nums:
            if num > 0:
                hashset.add(num)

        return len(hashset)

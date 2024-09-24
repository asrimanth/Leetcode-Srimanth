class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self.set_method(nums)
    
    
    def set_method(self, nums: List[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        hash_set = set()
        for num in nums:
            if num not in hash_set:
                hash_set.add(num)
            else:
                return num

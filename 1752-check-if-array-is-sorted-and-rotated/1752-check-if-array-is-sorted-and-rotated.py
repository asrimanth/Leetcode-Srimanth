class Solution:
    def check(self, nums: List[int]) -> bool:
        return self.dip_count(nums)

    def dip_count(self, nums: List[int]) -> bool:
        """
        Checks the number of dips in the array.
        If it exceeds 1, return False. Otherwise it is True.
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        n = len(nums)
        if n == 1:
            return True
        num_dips = 0
        for i in range(1, n):
            if nums[i-1] > nums[i]: # Previous num is strictly greater
                num_dips += 1
            if num_dips > 1:
                return False

        # Check if already sorted
        if num_dips == 0: return True
        # Check if num dips is 1 and 
        # makes sure that the list is ascending order even at the end points
        result_bool = (num_dips == 1 and nums[0] >= nums[n-1])
        return result_bool

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self.rabbit_and_hare_method(nums)
    
    def rabbit_and_hare_method(self, nums: List[int]) -> int:
        # Useful for cycle detection in linked lists
        # https://www.youtube.com/watch?v=wjYnzkAhcNk
        slow, fast = 0, 0
        while True:
            slow = nums[slow] # Advance slow once
            fast = nums[nums[fast]] # Advance fast twice
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        

    def set_method(self, nums: List[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        hash_set = set()
        for num in nums:
            if num not in hash_set:
                hash_set.add(num)
            else:
                return num

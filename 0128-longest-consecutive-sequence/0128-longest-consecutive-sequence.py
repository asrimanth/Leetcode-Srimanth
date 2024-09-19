class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_sequence_size = 0
        for num in numset:
            # Check if left neighbor does not exist
            if num-1 not in numset:
                # start of a sequence
                curr_sequence_size = 0
                temp = num
                while temp in numset: # Go until sequence end is reached.
                    curr_sequence_size += 1
                    temp += 1
                # Assign the appropriate max_size
                max_sequence_size = max(curr_sequence_size, max_sequence_size)
        return max_sequence_size

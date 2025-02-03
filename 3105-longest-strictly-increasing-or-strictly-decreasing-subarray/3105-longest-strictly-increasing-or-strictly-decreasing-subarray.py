class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        return self.my_solution(nums)

    def my_solution(self, nums: List[int]) -> int:
        """
        Maintain a list of sequence lengths by passing the array twice.
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        max_inc, max_dec = 0, 0
        N = len(nums)

        # Strictly increasing
        inc_seq_lens = []
        for i in range(N):
            prev = nums[i-1] if i-1 >= 0 else None
            prev, curr = nums[i-1], nums[i]
            if prev is not None and len(inc_seq_lens) and curr > prev:
                inc_seq_lens[-1] += 1
            else:
                inc_seq_lens.append(1)

        # Strictly decreasing
        dec_seq_lens = []
        for i in range(N):
            prev = nums[i-1] if i-1 >= 0 else None
            prev, curr = nums[i-1], nums[i]
            if prev is not None and len(dec_seq_lens) and curr < prev:
                dec_seq_lens[-1] += 1
            else:
                dec_seq_lens.append(1)

        # print(inc_seq_lens, dec_seq_lens)

        return max(max(inc_seq_lens), max(dec_seq_lens))

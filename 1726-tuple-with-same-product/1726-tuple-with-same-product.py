# Neetcode solution: https://www.youtube.com/watch?v=SSwvMoOhiq0
# Time Complexity: O(N^2)
# Space Complexity: O(N) for hashmap

from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int) # n1 * n2 -> count products
        # pairs_count = defaultdict(int) # n1 * n2 -> count pairs ((a, b), (c, d))

        # For every pair, we will have 8 possible tuples
        # ab,cd; ba,cd; ab,dc; ba,dc; cd,ab; dc,ab; cd,ba; dc,ba.
        # 1 count -> 0 pairs -> 0 tuples
        # 2 count -> 1 pair -> 8 tuples
        # 3 count -> 3 pairs -> 24 tuples
        # 4 count -> 6 pairs -> 48 tuples
        # 5 count -> 10 pairs -> 80 tuples
        # Math from count to pairs: count * (count-1) / 2

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                # pairs_count[product] += product_count[product]
                product_count[product] += 1
        
        result = 0
        for count in product_count.values():
            pairs = (count * (count-1)) // 2
            result += 8 * pairs
        return result

# Time Complexity: O(N)
# Space Complexity: O(N*K)

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.bucket_sort(nums, k)

    def bucket_sort(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        bucket = [list() for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            bucket[count].append(num)

        result = []
        for idx in range(len(bucket)-1, 0, -1):
            for num in bucket[idx]:
                result.append(num)
                if len(result) == k:
                    return result
        return result[:k]

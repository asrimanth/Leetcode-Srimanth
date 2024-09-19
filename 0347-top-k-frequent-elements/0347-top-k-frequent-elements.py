from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.bucket_sort_method(nums, k)
    
    def bucket_sort_method(self, nums: List[int], k: int) -> List[int]:
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        counts = dict(Counter(nums))
        buckets = [[] for i in range(len(nums)+1)]
        for num, count in counts.items():
            buckets[count].append(num)

        result = []
        for i in range(len(buckets)-1, -1, -1):
            nums_with_count_i = buckets[i]
            for num in nums_with_count_i:
                result.append(num)
                if len(result) == k:
                    return result
        return [None]

    def hash_map_method(self, nums: List[int], k: int) -> List[int]:
        # Time Complexity: O(n*log(n))
        # Space Complexity: O(n)
        hash_map = dict(Counter(nums))
        hash_map = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
        # Now it is a list of tuples
        return [item[0] for item in hash_map[:k]]

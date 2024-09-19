from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.hash_map_method(nums, k)
    
    def hash_map_method(self, nums: List[int], k: int) -> List[int]:
        # Time Complexity: O(n*log(n))
        # Space Complexity: O(n*log(n))
        hash_map = dict(Counter(nums))
        hash_map = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
        # Now it is a list of tuples
        return [item[0] for item in hash_map[:k]]

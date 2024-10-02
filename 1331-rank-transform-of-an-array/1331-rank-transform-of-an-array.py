class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # hashmap + sort
        hashmap = set(arr)
        hashmap = {item: idx+1 for idx, item in enumerate(sorted(hashmap))}
        rank = 1
        idx = 0
        for idx in range(len(arr)):
            arr[idx] = hashmap[arr[idx]]
        return arr

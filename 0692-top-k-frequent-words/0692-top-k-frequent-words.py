from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return self.solution_2(words, k)
    
    def solution_2(self, words: List[str], k: int) -> List[str]:
        # Bucket sort solution
        data = Counter(words)
        bucket = {i: [] for i in range(len(words))}
        for key, count in data.items():
            bucket[count].append(key)
        
        # Now sort the keys in the bucket lexicographically
        for count in bucket.keys():
            bucket[count].sort(reverse=True)
            # Reverse lexicographic since we will pop from last.

        result = []
        # Now query the bucket in reverse order
        for count in reversed(bucket.keys()):
            temp = len(bucket[count])
            while temp:
                result.append(bucket[count].pop())
                temp -= 1
                k -= 1
                if not k:
                    return result


    def solution_1(self, words: List[str], k: int) -> List[str]:
        # A solution in O(nlogn) using heaps/sorting
        words = sorted(words)
        data = Counter(words)
        data = sorted(data.items(), key = lambda x:x[1], reverse=True)
        data = [item for item, _ in data]
        return data[:k]

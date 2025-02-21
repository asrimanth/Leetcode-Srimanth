from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return self.solution_1(words, k)

    def solution_1(self, words: List[str], k: int) -> List[str]:
        # A solution in O(nlogn) using heaps/sorting
        words = sorted(words)
        data = Counter(words)
        data = sorted(data.items(), key = lambda x:x[1], reverse=True)
        data = [item for item, _ in data]
        return data[:k]

# Time Complexity: O(N * log(N)) + O(N * (K^3))
# Space Complexity: O(N + P)
from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = defaultdict(list)
        patterns = defaultdict(int)

        for u, t, w in zip(username, timestamp, website):
            data[u].append((t, w))
        
        for u in data.keys():
            data[u].sort()
            item = data[u]
            user_patterns = set() # Avoid counting duplicate patterns for the same user

            # Compute all possible sequences
            for i in range(len(item)):
                for j in range(i+1, len(item)):
                    for k in range(j+1, len(item)):
                        pattern = item[i][1], item[j][1], item[k][1]
                        if pattern not in user_patterns:
                            user_patterns.add(pattern)
                            patterns[pattern] += 1
        
        result = []
        temp = 0
        for patt, patt_count in patterns.items():
            if temp < patt_count:
                temp = patt_count
                result = patt
            elif temp == patt_count: # Equal patterns with largest score
                result = result if result < patt else patt
        return result

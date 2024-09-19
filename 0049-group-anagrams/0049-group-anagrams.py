# len(str) = k
# Time Complexity: O(n * k*log(k))
# Space Complexity: O(n*k)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in result:
                result[sorted_word].append(word)
            else:
                result[sorted_word] = [word]
        return result.values()

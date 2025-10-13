from collections import Counter, defaultdict
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        return self.result_array(words)

    def result_array(self, words: List[str]) -> List[str]:
        # Time Complexity: O(N * K), K = len(each_word)
        # Space Complexity: O(N) for result
        n = len(words)
        result = [words[0]]
        i = 1
        for curr_word in words:
            last_word = result[-1]
            if not self.are_anagrams_hashmap_2(last_word, curr_word):
                result.append(curr_word)
        return result

    def are_anagrams_hashmap_2(self, string1: str, string2: str) -> bool:
        # Anagram Time Complexity: O(K)
        # Anagram Space Complexity: O(K)
        if len(string1) != len(string2):
            return False
        
        counts = defaultdict(int)
        for char in string1:
            counts[char] += 1
        
        for char in string2:
            counts[char] -= 1
            if counts[char] < 0:
                return False
        
        return True if counts else False

    def are_anagrams_hashmap_1(self, string1: str, string2: str) -> bool:
        # Anagram Time Complexity: O(K)
        # Anagram Space Complexity: O(K) + O(K) = O(K)
        if len(string1) != len(string2):
            return False
        return Counter(string1) == Counter(string2)

    def are_anagrams_sort(self, string1: str, string2: str) -> bool:
        # Anagram Time Complexity: O(K * log(K))
        # Anagram Space Complexity: O(K) + O(K) = O(K)
        if len(string1) != len(string2):
            return False
        return sorted(prev) == sorted(curr)

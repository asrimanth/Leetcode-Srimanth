# Time Complexity: O(N)
# Space Complexity: O(N)
from collections import Counter
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_counts = Counter(words)
        result = 0
        central = False
        for word, count in word_counts.items():
            complement = word[::-1]
            a, b = word[0], word[1]
            # if the word is a palindrome
            if a == b:
                if count % 2 == 0: # Even number of elements
                    result += count
                else:
                    result += count - 1
                    central = True
            # consider a pair of non-palindrome words,
            # such that one is the reverse of another
            # b+a is the reversed word
            elif a < b:
                result += 2 * min(count, word_counts[b + a])

        if central:
            result += 1
        return 2 * result

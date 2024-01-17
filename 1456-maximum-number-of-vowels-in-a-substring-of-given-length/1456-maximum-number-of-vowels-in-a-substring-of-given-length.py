class Solution:
    def get_vowel_count(self, sub_str, vowels):
        count = 0
        for char in sub_str:
            count += int(char in vowels)
        return count

    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        vowels = {"a", "e", "i", "o", "u"}
        if len(s) == k:
            return self.get_vowel_count(s, vowels)
        count = self.get_vowel_count(s[:k], vowels)
        max_count = count
        # print(f"Initail count {s[k]}: {count}")
        for i in range(len(s)-k):
            prev_char = s[i]
            latest = s[i+k]
            if prev_char in vowels and latest not in vowels:
                count -= 1
            elif prev_char not in vowels and latest in vowels:
                count += 1
            max_count = max(count, max_count)
            # print(f"Previous, latest, prev_idx, latest_idx = {prev_char} {latest} {i}, {i+k}")
            # print(f"count at window {s[i:i+k]}: {count}")
        return max_count
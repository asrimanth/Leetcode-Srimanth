from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)
        # Create a dict structure
        # Use ascii
        s1_map = {str(chr(num)): 0 for num in range(97, 123)}
        for char in s1:
            s1_map[char] += 1
        counts = {str(chr(num)): 0 for num in range(97, 123)}
        for char in s2[:window_len]:
            counts[char] += 1
        if s1_map == counts:
            return True
        self.print_dicts(s1, s2[:window_len], s1_map, counts)
        left = 0
        for right in range(window_len, len(s2)):
            counts[s2[left]] -= 1
            if s1_map == counts:
                return True
            counts[s2[right]] += 1
            if s1_map == counts:
                return True
            # print(left, right, s1, s2[left:right])
            # self.print_dicts(s1, s2[left:right], s1_map, counts)
            left += 1
        return False

    def print_dicts(self, temp1, temp2, count1, count2):
        print({key: count1[key] for key in temp1})
        print({key: count2[key] for key in temp2})
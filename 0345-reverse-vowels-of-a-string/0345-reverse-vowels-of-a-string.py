class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # result = ""
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        if len(s) <= 1:
            return s
        # Two pointer approach
        st_list = list(s)
        left = 0
        right = len(st_list) - 1
        while left < right:
            if st_list[left] in vowels and st_list[right] in vowels:
                st_list[left], st_list[right] = st_list[right], st_list[left]
                left += 1
                right -= 1
            elif st_list[left] in vowels:
                right -= 1
            elif st_list[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1
        return "".join(st_list)
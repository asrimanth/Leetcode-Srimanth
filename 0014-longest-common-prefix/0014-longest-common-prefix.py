class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        data = sorted(strs)
        first, last = data[0], data[-1]
        result = ""
        length = min(len(first), len(last))
        for i in range(length):
            if first[i] == last[i]:
                result += first[i]
            else:
                break
        return result
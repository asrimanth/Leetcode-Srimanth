class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        for i in range(0, len(s)-k+1, k):
            result.append(s[i:i+k])
        mod = len(s)%k
        remaining_count = k - mod
        if mod != 0:
            last_idx = len(s)-k+1
            last_str = str(s[last_idx+1]) + "".join([f"{fill}" * remaining_count])
            result.append(last_str)
        return result

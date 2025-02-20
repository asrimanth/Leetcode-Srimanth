class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)
        n = len(nums)

        def backtrack(temp):
            if len(temp) == n:
                if temp not in nums:
                    return temp
                return ""
            for bit in ["0", "1"]:
                # Append bits and pop for backtracking
                result = backtrack(temp + bit)
                if result:
                    return result

        result = backtrack("")
        return result

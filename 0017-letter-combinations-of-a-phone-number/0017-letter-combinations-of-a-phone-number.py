# Time Complexity: O(3^n) or O(4^n)
#n is length of input string. Each digit has 3 or 4 letters. For example, if you get "23"(n) as input string, we will create 9 combinations which is O(3^2) = 9
# Space complexity: O(n) for internal stack of the recursive function.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return result
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        def backtrack(idx, comb):
            if idx == len(digits):
                result.append(comb)
                return
            for letter in mapping[digits[idx]]:
                backtrack(idx+1, comb + letter)
        backtrack(0, "")
        return result

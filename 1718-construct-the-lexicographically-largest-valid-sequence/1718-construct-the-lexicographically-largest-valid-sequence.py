# Neetcode Solution: Backtracking + Greedy
# Greedy part: Start building the backtracking tree from the largest number.
# The first solution will be the largest.
# Time Complexity: O(N!)
# Actual runtime is much lower, since we return once we find the 1st sequence.
# Space Complexity: O(N)
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # Expected length is 2n-1
        result = [0] * ((2*n) - 1)
        used = set()

        def backtrack(i):
            if i == len(result):
                return True
            
            # Try largest elements: n....1 (n and 1 inclusive)
            for num in range(n, 0, -1):
                # validation
                if num in used:
                    continue
                # result[i+num] => the array at i+num is not 0
                # Check for out of bounds in case of numbers other than 1
                if num > 1 and (i+num >= len(result) or result[i+num]):
                    continue
                
                # Try the decision
                used.add(num)
                result[i] = num
                if num > 1:
                    result[i+num] = num

                j = i + 1
                while j < len(result) and result[j]:
                    j += 1

                # Recursive Step:
                if backtrack(j):
                    return True

                # Backtrack and undo the current decision
                used.remove(num)
                result[i] = 0
                if num > 1:
                    result[i+num] = 0
            return False

        backtrack(0)
        return result

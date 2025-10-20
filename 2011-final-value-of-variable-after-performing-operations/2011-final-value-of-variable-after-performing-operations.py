class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        mapping = {"++X": 1, "X++": 1, "--X": -1, "X--": -1}
        result = 0
        for op in operations:
            result += mapping[op]
        return result

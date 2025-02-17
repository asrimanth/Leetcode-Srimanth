from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return self.neetcode_solution(tiles)

    def neetcode_solution(self,  tiles: str) -> int:
        counts = Counter(tiles)

        def backtrack():
            result = 0

            for char in counts.keys():
                if counts[char] > 0:
                    counts[char] -= 1 # Make a move
                    result += 1 # Consider current combo
                    result += backtrack() # backtrack
                    counts[char] += 1 # Undo the move
            return result

        return backtrack()

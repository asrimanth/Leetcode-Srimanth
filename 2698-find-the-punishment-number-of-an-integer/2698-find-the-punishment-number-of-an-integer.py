class Solution:
    def punishmentNumber(self, n: int) -> int:
        return self.neetcode_solution(n)
    
    def neetcode_solution(self, n: int) -> int:
        """
        From editorial:
        Time Complexity: O(N*2^log(N)) for backtracking
        Space Complexity: O(log(N))
        https://www.youtube.com/watch?v=LWgksJP-5SA
        """
        def partition(i: int, curr: int, target: int, string: str):
            if i == len(string) and curr == target:
                return True
            
            for j in range(i, len(string)):
                if partition(j+1, curr + int(string[i:j+1]), target, string):
                    return True
            return False
        
        result = 0
        for i in range(1, n+1):
            if partition(0, 0, i, str(i*i)):
                result += i*i
        return result

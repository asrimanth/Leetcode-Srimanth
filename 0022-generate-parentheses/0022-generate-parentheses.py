class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # DFS recursive
        # https://leetcode.com/problems/generate-parentheses/discuss/1561062/Python3-or-Recursive-approach-or-Simple-Logic-or-Step-by-step-explanation
        def dfs(res, string, left, right):
            if left == 0 and right == 0:
                res.append(string)
            
            if left > 0:
                dfs(res, string + "(", left-1, right)
            
            if right > 0 and left < right:
                dfs(res, string + ")", left, right-1)
            
        res = []
        dfs(res, "", n, n)
        return res
        
class Solution(object):
    
    def isInsideCircle(self, a, b, x, y, r):
        return ((x-a) ** 2 + (y-b) ** 2) <= r ** 2
    
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        answers = []
        for x, y, r in queries:
            count = 0
            for a, b in points:
                count += int(self.isInsideCircle(a, b, x, y, r))
            answers.append(count)
        return answers
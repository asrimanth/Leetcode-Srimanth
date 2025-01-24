# Time Complexity: O(E + V)
# Space Complexity: O(E + V)

from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}
        result = []

        def dfs(node):
            if node in safe:
                return safe[node]
            # Check recursively if any of the neighbors are not safe\
            safe[node] = False
            for nei in graph[node]:
                if not dfs(nei): # One of the leaf nodes is not safe
                    return safe[node]
            # All neighbors checked, now it is safe.
            safe[node] = True
            return True

        for i in range(n):
            if dfs(i):
                result.append(i)
        return result

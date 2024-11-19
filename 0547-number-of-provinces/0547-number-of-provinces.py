# Time Complexity: O(N^2) because we potentially check every connection between the cities in the isConnected matrix. 
#Each city is visited once, and for each visit, we could traverse its connections, leading to a quadratic time complexity.
# Space Complexity: O(N)

from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for neigh, connected in enumerate(isConnected[node]):
                if connected and (neigh not in visited):
                    visited.add(neigh)
                    dfs(neigh)

        num_provinces = 0
        visited = set()
        for city in range(len(isConnected)):
            if city not in visited:
                visited.add(city)
                dfs(city)
                num_provinces += 1

        return num_provinces

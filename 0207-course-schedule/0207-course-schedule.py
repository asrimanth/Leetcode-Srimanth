# Time Complexity: O(N*(N + P)), N = numCourses, P = numPrerequisites
# N+P for DFS, doing DFS N times.
# Space Complexity: O(N) * (O(N) [visited] + O(N) [recursion stack])

from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list
        pre_map = defaultdict(list)
        for course, prereq in prerequisites:
            pre_map[course].append(prereq)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if pre_map[course] == []:
                return True
            
            # First, add course to visited
            visited.add(course)
            # Explore neighbours
            for prereq in pre_map[course]:
                if not dfs(prereq): return False
            
            # Once we visited all neighbours
            visited.remove(course)
            pre_map[course] = [] # The course can be taken
            return True

        # Need to do this for every course since we can have disjoint graphs
        # Ex: 1 -> 2, 3 -> 4
        for course in range(numCourses):
            if not dfs(course): return False
        return True

from collections import deque, defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        return self.optimized_solution(numCourses, prerequisites, queries)
        
    def optimized_solution(self, num_courses: int, prereqs: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        Optimized solution from Neetcode: https://www.youtube.com/watch?v=wYoZMBenHYY
        Idea: Perform DFS and store the graph data in a hashmap of node: set
        This will make querying O(1)
        Time Complexity: O(N*(N+P)) + O(Q)
        Space Complexity: O(N)
        Why O(N*(N+P)): The N is for union operation over the sub dependencies.
        """

        # Create adjacency list
        adj_list = defaultdict(list)
        for prereq, course in prereqs:
            adj_list[course].append(prereq)

        pre_req_map = defaultdict(set) # map course -> set(prereqs)
        # Perform DFS
        def dfs(course):
            if course not in pre_req_map:
                pre_req_map[course] = set()
                for prereq in adj_list[course]:
                    pre_req_map[course] = pre_req_map[course] | dfs(prereq) # Performs Union of sets
                pre_req_map[course].add(course)
            return pre_req_map[course]

        for course in range(num_courses):
            dfs(course)

        result = []
        for u, v in queries:
            result.append(u in pre_req_map[v])
        return result

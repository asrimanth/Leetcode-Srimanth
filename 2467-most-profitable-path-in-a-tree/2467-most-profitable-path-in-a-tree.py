# Neetcode solution: https://www.youtube.com/watch?v=mESeQZKfvtY
# Time Complexity: O(N)
# Space Complexity: O(N)
from collections import defaultdict, deque

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        # Bob Simulation - DFS
        bob_times = {}
        def dfs(src, prev, time):
            if src == 0: # Reached the root
                bob_times[src] = time
                return True
            for nei in adj[src]:
                if nei == prev: # Don't revisit the prev node
                    continue
                if dfs(nei, src, time+1):
                    bob_times[src] = time
                    return True
            return False
        dfs(bob, -1, 0)

        # Alice Simulation - BFS
        fringe = deque([(0, 0, -1, amount[0])]) # Node, time, parent, profit_so_far
        result = float("-inf")
        while fringe:
            curr_node, curr_time, parent, curr_profit = fringe.popleft()

            for nei in adj[curr_node]:
                if nei == parent: # Don't revisit the parent
                    continue
                nei_profit = amount[nei]
                nei_time = curr_time + 1
                if nei in bob_times: # Bob has visited
                    if nei_time > bob_times[nei]: # Bob visited first, hence their time is low.
                        nei_profit = 0
                    elif nei_time == bob_times[nei]: # Both visited at the same time
                        nei_profit //= 2 # Int divide current profit by 2
                fringe.append((nei, nei_time, curr_node, curr_profit + nei_profit))

                # Update result here, not at the top
                # Since root can have a single neighbor
                if len(adj[nei]) == 1: # Node has exactly one neighbor
                    result = max(result, curr_profit + nei_profit)
        return result

# Time Complexity: O(M*log(M)) + O(N*log(N)) + O(M*N)
# Space Complexity: O(N)

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        results = [0] * len(queries)
        logs.sort(key=lambda x:x[1])
        queries = [(q, idx) for idx, q in enumerate(queries)]
        queries.sort(key=lambda x:x[0])
        left, right = 0, 0
        m = len(logs)

        num_servers_in_window = defaultdict(int)

        # For each query;
        # Find a window of that contains servers whose processing time  is within query interval
        for end, idx in queries:
            start = end - x

            while right < m and logs[right][1] <= end:
                num_servers_in_window[logs[right][0]] += 1
                right += 1
            
            while left < right and logs[left][1] < start:
                num_servers_in_window[logs[left][0]] -= 1
                if num_servers_in_window[logs[left][0]] == 0:
                    del num_servers_in_window[logs[left][0]]
                left += 1
            
            results[idx] = n - len(num_servers_in_window)
    
        return results

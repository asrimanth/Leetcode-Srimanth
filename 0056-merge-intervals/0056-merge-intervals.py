# Time Complexity: O(N*log(N))
# Space Complexity: O(N) for result

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by start time
        intervals = sorted(intervals, key=lambda x: x[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            prev_interval = result[-1]
            curr_interval = intervals[i]
            if prev_interval[1] >= curr_interval[0]:
                start = min(prev_interval[0], curr_interval[0])
                end = max(prev_interval[1], curr_interval[1])
                result[-1] = [start, end]
            else:
                result.append(curr_interval)
        return result

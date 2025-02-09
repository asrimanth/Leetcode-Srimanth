class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort by start value
        intervals = sorted(intervals, key= lambda x: x[0])
        n = len(intervals)
        i = 1
        prev = intervals[0]
        while i < n:
            # cases:
            # 1. start is between prev start and prev end
            # 2. start is after prev end
            old_start, old_end = intervals[i-1]
            start, end = intervals[i]
            if old_start <= start <= old_end:
                new_val = [min(old_start, start), max(old_end, end)]
                intervals[i-1] = new_val
                del intervals[i]
                n -= 1
            else:
                i += 1
        return intervals

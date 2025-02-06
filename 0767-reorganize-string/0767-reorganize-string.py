# Time Complexity: O(N*log(N))
# Space Complexity: O(N)

from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = Counter(s)
        max_heap = []
        max_heap = [(-value, key) for key, value in char_count.items()]
        heapq.heapify(max_heap)

        max_occur = -1 * max_heap[0][0]
        result = ""
        if max_occur > (len(s) + 1) // 2:
            return result

        previous = None

        while max_heap:
            prev_char = "" if not len(result) else result[-1]
            count, curr_char = heapq.heappop(max_heap)
            result += curr_char
            count += 1
            if previous:
                # Only push the previous last char to heap when count still left 
                # and after another char has been added
                heapq.heappush(max_heap, previous)
            previous = (count, curr_char) if count < 0 else None
        return result

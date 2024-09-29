# Time Complexity: O(M+N)
# Space Complexity: O(M+N) if no common intervals

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []

        while i < len(firstList) and j < len(secondList):
            # If 2 intervals are equal
            if firstList[i] == secondList[j]:
                result.append(firstList[i])
                i += 1
                j += 1
                continue
            # If start of ith is smaller than start of jth
            # And start of ith < end of jth
            head1, tail1 = firstList[i][0], firstList[i][1]
            head2, tail2 = secondList[j][0], secondList[j][1]
            head = max(head1, head2)
            tail = min(tail1, tail2)
            if head <= tail:
                result.append([head, tail])
            if tail1 <= tail2:
                i += 1
            else:
                j += 1
        return result

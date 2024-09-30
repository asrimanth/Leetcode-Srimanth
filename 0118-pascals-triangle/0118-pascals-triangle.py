class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        if numRows == 1:
            return result
        for _ in range(1, numRows):
            new_row = [1]
            prev_row = result[-1]
            for idx in range(1, len(prev_row)):
                a, b = prev_row[idx-1], prev_row[idx]
                new_row.append(a+b)
            new_row.append(1)
            result.append(new_row)
        return result

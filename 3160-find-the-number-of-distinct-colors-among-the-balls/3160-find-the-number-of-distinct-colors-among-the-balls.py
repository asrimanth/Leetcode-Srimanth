from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = dict()
        mapping = dict()
        result = []

        for idx, color in queries:
            # 4 cases:
            # 1. ball is new and new color
            # 2. ball is new and existing color
            # 3. ball is already colored and new color
            # 4. ball is already color and from existing colors
            if idx in balls:
                prev_color = balls[idx]
                mapping[prev_color] -= 1
                if mapping[prev_color] <= 0:
                    del mapping[prev_color]
            mapping[color] = mapping.get(color, 0) + 1
            balls[idx] = color

            result.append(len(mapping.keys()))
        return result

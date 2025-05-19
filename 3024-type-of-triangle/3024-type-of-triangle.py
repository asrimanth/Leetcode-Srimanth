# Time Complexity: O(1)
# Space Complexity: O(1)
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if len(nums) != 3:
            return "none"

        a, b, c = nums
        if a == b == c:
            return "equilateral"
        elif a + b > c and b + c > a and c + a > b:
            if a == b or b == c or c == a:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"

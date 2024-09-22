class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            if height[left] < height[right]:
                is_left_min = True
                min_height = height[left]
            else:
                is_left_min = False
                min_height = height[right]
            curr_area = min_height * (right - left)
            max_area = max(curr_area, max_area)
            if is_left_min:
                left += 1
            else:
                right -= 1
        return max_area

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        left = 0
        right = len(height) - 1
        
        while left != right:
            current_water_vol = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, current_water_vol)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_water
use std::cmp::max;
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        // Time Complexity: O(N)
        // Space Complexity: O(1)
        let mut left = 0;
        let mut right = height.len() - 1;
        let mut min_height = 0;
        let mut max_area = 0;
        let mut is_left_min = false;
        while left < right {
            if height[left] < height[right] {
                is_left_min = true;
                min_height = height[left]
            }
            else {
                is_left_min = false;
                min_height = height[right];
            }
            let curr_area = min_height * ((right - left) as i32);
            max_area = max(max_area, curr_area);
            if is_left_min {
                left += 1;
            }
            else {
                right -= 1;
            }
        }
        return max_area;
    }
}

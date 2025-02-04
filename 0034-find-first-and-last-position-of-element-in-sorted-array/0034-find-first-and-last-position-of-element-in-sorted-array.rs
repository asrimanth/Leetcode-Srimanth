// Time Complexity: O(log(N))
// Space Complexity: O(1)
impl Solution {
    
    pub fn binary_search(nums: &Vec<i32>, key: i32, is_low: bool) -> i32 {
        let mut left = 0;
        let mut right = nums.len() as i32 - 1;
        let mut result = -1; // Store the result index

        while left <= right {
            let mid = left + (right - left) / 2; // Avoid potential overflow
            if nums[mid as usize] == key {
                result = mid; // Update result when key is found
                if is_low {
                    right = mid - 1; // Narrow search to the left for lower bound
                } else {
                    left = mid + 1; // Narrow search to the right for upper bound
                }
            } else if nums[mid as usize] > key {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        result
    }

    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
        if nums.len() == 0 {
            return Vec::<i32>::from([-1, -1]);
        }
        let start_pos = Self::binary_search(&nums, target, true);
        let end_pos = Self::binary_search(&nums, target, false);
        Vec::<i32>::from([start_pos, end_pos])
    }
}
use std::cmp::{min, max};
impl Solution {
    pub fn max_increasing_subarrays(nums: Vec<i32>) -> i32 {
        // Time Complexity: O(N)
        // Space Complexity: O(1)
        let n = nums.len();
        let (mut prev, mut curr, mut result) = (0, 1, 0);
        for i in 1..n {
            if nums[i] > nums[i-1] {
                curr += 1
            }
            else {
                prev = curr;
                curr = 1;
            }
            let possibility_one = min(prev, curr); // Minimum of 2 subsequences
            let possibility_two = (curr / 2) as i32; // Current sequence can be treated as 2 subsequences
            result = max(result, max(possibility_one, possibility_two));
        }
        return result;
    }
}
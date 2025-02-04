// Time Complexity: O(N)
// Space Complexity: O(1)

use std::cmp::max;
impl Solution {
    pub fn max_ascending_sum(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut curr_sum = nums[0];
        let mut max_sum = curr_sum;

        for i in (1..n){
            if nums[i] > nums[i-1] {
                curr_sum += nums[i]
            }
            else {
                curr_sum = nums[i]
            }
            max_sum = max(max_sum, curr_sum);
        }
        max_sum
    }
}

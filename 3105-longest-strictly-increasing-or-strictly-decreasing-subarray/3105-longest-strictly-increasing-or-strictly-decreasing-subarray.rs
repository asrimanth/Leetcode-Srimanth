use std::cmp::max;
impl Solution {
    pub fn longest_monotonic_subarray(nums: Vec<i32>) -> i32 {
        // An elegant solution I found in Neetcode comment section.
        // The code is self explanatory.
        // Time Complexity: O(N)
        // Space Complexity: O(1)
        let mut longest = 1;
        let mut inc = 1;
        let mut dec = 1;
        let N = nums.len();
        for i in (1..N) {
            if nums[i] > nums[i-1] {
                inc = inc + 1;
                dec = 1;
            }
            else if nums[i] < nums[i-1] {
                dec = dec + 1;
                inc = 1;
            }
            else {
                inc = 1;
                dec = 1;
            }
            longest = max(longest, max(inc, dec));
        }
        longest
    }
}

// Explanation here: https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/solutions/7273333/simple-solution-o-n-time-o-1-space-beats-100-solutions-detailed-explanation

impl Solution {
    pub fn has_increasing_subarrays(nums: Vec<i32>, k: i32) -> bool {
        // Time Complexity: O(N)
        // Space Complexity: O(1)
        let mut prev = 0;
        let mut curr = 1;
        let n = nums.len();
        let k2 = 2 * k;
        for i in 1..n {
            if nums[i] > nums[i-1] {
                curr += 1;
            }
            else { // Curr sequence broke
                prev = curr; // Send curr sequence length to prev
                curr = 1; // Start a new sequence
            }
            if (prev >= k && curr >= k) || curr >= k2 {
                return true;
            }
        }
        return false;
    }
}

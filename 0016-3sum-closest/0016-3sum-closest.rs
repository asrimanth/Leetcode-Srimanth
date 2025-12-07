// Time Complexity: O(N^2)
// Space Complexity: O(1)
impl Solution {
    pub fn three_sum_closest(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();
        let mut numbers = nums;
        numbers.sort();
        let mut min_diff: i32 = 99999999;
        let mut result: i32 = 0;
        for i in 0..n {
            let mut left = i+1;
            let mut right = n-1;
            // Two pointer approach
            while left < right {
                let (num1, num2, num3) = (numbers[i], numbers[left], numbers[right]);
                let total = num1 + num2 + num3;
                let diff = total - target;
                if diff.abs() < min_diff {
                    min_diff = diff.abs();
                    result = total;
                }
                if total > target {
                    right -= 1;
                }
                else {
                    left += 1;
                }
            }
        }
        return result;
    }
}
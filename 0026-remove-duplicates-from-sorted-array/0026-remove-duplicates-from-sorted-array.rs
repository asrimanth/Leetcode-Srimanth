impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        if nums.is_empty() {
            return 0;
        }
        let mut insert_idx = 1;
        for i in 1..nums.len() {
            if nums[i] != nums[i-1] {
                nums[insert_idx] = nums[i];
                insert_idx += 1;
            }
        }
        insert_idx as i32
    }
}
use std::collections::HashSet;
impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut uniq_nums = HashSet::new();
        for num in nums {
            if uniq_nums.contains(&num) {
                return true;
            }
            else {
                uniq_nums.insert(num);
            }
        }
        return false;
    }
}

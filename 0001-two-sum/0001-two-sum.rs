use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        return Self::hash_map_solution(nums, target);
    }

    pub fn hash_map_solution(nums: Vec<i32>, target: i32) -> Vec<i32> {
        // Time Complexity: O(N)
        // Space Complexity: O(N)
        let n: usize = nums.len();
        let mut hashmap: HashMap<i32, i32> = HashMap::new();

        for i in 0..n {
            let (current, complement) = (nums[i], target - nums[i]);
            if hashmap.contains_key(&complement){
                let comp_index = hashmap[&complement];
                return Vec::from([i as i32, comp_index as i32]);
            }
            hashmap.entry(current).or_insert(i as i32);
        }
        return Vec::new();
    }

    pub fn brute_force_solution(nums: Vec<i32>, target: i32) -> Vec<i32> {
        // Time Complexity: O(N ** 2)
        // Space Complexity: O(1)
        let n: usize = nums.len();
        for i in 0..n {
            for j in i+1..n{
                if nums[i] + nums[j] == target {
                    return Vec::from([i as i32, j as i32]);
                }
            }
        }
        return Vec::new();
    }
}
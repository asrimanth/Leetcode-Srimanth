// Time Complexity: O(N)
// Space Complexity: O(N)

use std::collections::HashMap;
use std::cmp::max;
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut chars_idx_map: HashMap<char, usize> = HashMap::new();
        let mut left: i32 = -1;
        let mut result = 0;

        for (right, ch) in s.chars().enumerate() {
            match chars_idx_map.get(&ch) {
                Some(idx) => left = max(left, *idx as i32),
                None => (),
            };

            result = max(result, right as i32 - left);
            chars_idx_map.insert(ch, right);
        }

        result
    }
}

// Time Complexity: O(2 * N) = O(N)
// Space Complexity: O(N)
use std::collections::HashMap;
use std::cmp::max;
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut left = 0;
        let mut right = 0;
        let mut char_counts = HashMap::new();
        let mut result = 0;
        // Using enumerate to iterate over chars with their indices
        for (right, rchar) in s.chars().enumerate() {
            // Get the count for the current character
            let count = char_counts.entry(rchar).or_insert(0);
            *count += 1;

            // While there is a duplicate character, shrink the window from the left
            while *char_counts.get(&rchar).unwrap() > 1 {
                // Get the character at the left pointer
                let lchar = s.chars().nth(left).unwrap();
                char_counts.entry(lchar).and_modify(|c| *c -= 1);
                left += 1;
            }
            result = max(result, (right - left + 1) as i32);
        }
        result
    }
}
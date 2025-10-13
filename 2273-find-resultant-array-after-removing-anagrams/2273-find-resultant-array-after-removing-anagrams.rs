use std::collections::HashMap;
impl Solution {
    pub fn remove_anagrams(words: Vec<String>) -> Vec<String> {
        // Time Complexity: O(N * K), K = len(each_word)
        // Space Complexity: O(N)
        let n = words.len();
        let mut result: Vec<String> = vec![words[0].clone()];
        let mut i: usize = 1;

        for i in 1..n {
            let last_in_result = result.last().unwrap();
            let curr = &words[i];
            if !Self::are_anagrams_hashmap_2(last_in_result, curr) {
                result.push(curr.clone());
            }
        }

        result
    }

    pub fn are_anagrams_hashmap_2(string1: &str, string2: &str) -> bool {
        // Anagram Time Complexity: O(K)
        // Anagram Space Complexity: O(K)
        if string1.len() != string2.len() {
            return false;
        }

        let mut char_counts = HashMap::new();
        for c in string1.chars() { // Increment counts for string1
            *char_counts.entry(c).or_insert(0) += 1;
        }
        for c in string2.chars() { // Decrement counts for string2
            let count = char_counts.entry(c).or_insert(0);
            *count -= 1;
            if *count < 0 {
                return false;
            }
        }

        // Check if remaining elements are non-zero. Return accordingly
        char_counts.values().all(|&count| count == 0)
    }

    pub fn are_anagrams_hashmap_1(string1: &str, string2: &str) -> bool {
        // Anagram Time Complexity: O(K)
        // Anagram Space Complexity: O(K) + O(K) = O(K)
        if string1.len() != string2.len() {
            return false;
        }

        let mut char_counts_1 = HashMap::new();
        let mut char_counts_2 = HashMap::new();
        for c in string1.chars() {
            *char_counts_1.entry(c).or_insert(0) += 1;
        }
        for c in string2.chars() {
            *char_counts_2.entry(c).or_insert(0) += 1;
        }

        char_counts_1 == char_counts_2
    }

    pub fn are_anagrams_sort(string1: &str, string2: &str) -> bool {
        // Anagram Time Complexity: O(K * log(K))
        // Anagram Space Complexity: O(K) + O(K) = O(K)
        if string1.len() != string2.len() {
            return false;
        }
        let mut chars1: Vec<char> = string1.chars().collect();
        let mut chars2: Vec<char> = string2.chars().collect();

        chars1.sort();
        chars2.sort();

        return chars1 == chars2;
    }
}
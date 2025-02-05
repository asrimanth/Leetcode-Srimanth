// Time Complexity: O(N)
// Space Complexity: O(1)
impl Solution {
    pub fn are_almost_equal(s1: String, s2: String) -> bool {
        let mut ptr_1: i32 = -1;
        let mut ptr_2: i32 = -1;
        let mut diff_count: i32 = 0;
        let n = s1.len();

        for i in (0..n) {
            if s1.chars().nth(i) != s2.chars().nth(i) {
                diff_count += 1;
                if ptr_1 == -1 { ptr_1 = i as i32; }
                else if ptr_2 == -1 { ptr_2 = i as i32; }
            }
        }
        if diff_count == 0 {
            return true;
        }
        let i = ptr_1 as usize;
        let j = ptr_2 as usize;
        diff_count == 2 && s1.chars().nth(i) == s2.chars().nth(j) && s1.chars().nth(j) == s2.chars().nth(i)
    }
}

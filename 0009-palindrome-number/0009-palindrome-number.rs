impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        return Self::reverse_num(x);
    }

    pub fn reverse_num(x: i32) -> bool {
        // Time Complexity: Number of digits in x = O(log10(x))
        // Space Complexity: O(1)
        if x < 0 || (x % 10 == 0 && x != 0) {
            // Handle negative numbers or numbers ending in 0 (except 0 itself)
            return false;
        }
        let mut temp: i32 = x;
        let mut x_rev: i32 = 0;
        while temp > 0 {
            let digit: i32 = temp % 10;
            x_rev = (x_rev * 10) + digit;
            temp = (temp / 10) as i32;
        }
        if x == x_rev {
            return true;
        }
        else {
            return false;
        }
    }

    pub fn str_approach(x: i32) -> bool {
        // Time Complexity: Number of digits in x = O(log10(x))
        // Space Complexity: O(1)
        if x < 0 || (x % 10 == 0 && x != 0) {
            // Handle negative numbers or numbers ending in 0 (except 0 itself)
            return false;
        }
        let xstr: String = x.to_string();
        let xstr_rev: String = xstr.chars().rev().collect();
        return xstr == xstr_rev;
    }
}

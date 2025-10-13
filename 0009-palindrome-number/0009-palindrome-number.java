class Solution {
    public boolean isPalindrome(int x) {
        if ((x < 0) || (x % 10 == 0 && x != 0)) {
            // Handle negative numbers or numbers ending in 0 (except 0 itself)
            return false;
        }
        return strApproach(x);
    }

    public boolean reverseNum(int x) {
        // Time Complexity: Number of digits in x = O(log10(x))
        // Space Complexity: O(1)
        int temp = x;
        int x_rev = 0;
        while (temp > 0) {
            int digit = temp % 10;
            x_rev = (x_rev * 10) + digit;
            temp = (int) (temp / 10);
        }
        if (x == x_rev) {
            return true;
        }
        else {
            return false;
        }
    }

    public boolean strApproach(int x) {
        // Time Complexity: Number of digits in x = O(log10(x))
        // Space Complexity: O(1)
        String xstr = Integer.toString(x);
        String xstr_rev = new StringBuffer(xstr).reverse().toString();
        return xstr.equals(xstr_rev);
    }
}
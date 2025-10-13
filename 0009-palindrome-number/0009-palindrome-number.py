class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            # Handle negative numbers or numbers ending in 0 (except 0 itself)
            return False
        return self.reverse_num(x)

    def reverse_num(self, x: int) -> bool:
        # Time Complexity: Number of digits in x = O(log10(x))
        # Space Complexity: O(1)
        temp = x
        x_rev = 0
        while temp:
            digit = temp % 10
            x_rev = x_rev*10 + digit
            temp = temp // 10
        if x == x_rev:
            return True
        else:
            return False

    def str_approach(self, x: int) -> bool:
        # Time Complexity: Number of digits in x = O(log10(x))
        # Space Complexity: O(1)
        x = str(x)
        return x == x[::-1]

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return self.two_pointer(x)

    def two_pointer(self, x: int) -> bool:
        # Time Complexity: Number of digits in x = O(log10(x))
        # Space Complexity: O(1)
        if x < 0:
            return False
        div = 1
        while x > 10 * div:
            div *= 10
        # Two pointer approach -  div from left and mod from right
        while x:
            if x // div != x % 10:
                return False
            x = (x % div) // 10
            div = div / 100
        return True

    def reverse_num(self, x: int) -> bool:
        # Time Complexity: Number of digits in x = O(log10(x))
        # Space Complexity: O(1)
        if x < 0:
            return False
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
        if x < 0:
            return False
        x = str(x)
        return x == x[::-1]

# Time Complexity: O(N*loglogN)#[Sieve] + O(right-left)
# Space Complexity: O(N), N = Right

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Precompute prime table until number right
        # Sieve of Eratosthenes
        
        primes = [True for i in range(right+1)]
        primes[0], primes[1] = False, False
        p = 2
        while p*p <= right:
            if primes[p]:
                # Mark all multiples of p as non-prime
                for i in range(p*p, right+1, p):
                    primes[i] = False
            p += 1

        prime_nums = [p for p in range(left, right+1) if primes[p]]
        result = (-1, -1)
        print(prime_nums)
        if len(prime_nums) < 2:
            return result

        min_diff = float("inf")
        for i in range(1, len(prime_nums)):
            difference = prime_nums[i] - prime_nums[i-1]
            print(prime_nums[i-1], prime_nums[i], min_diff, difference)
            if difference < min_diff:
                min_diff = difference
                result = (prime_nums[i-1], prime_nums[i])
        return result

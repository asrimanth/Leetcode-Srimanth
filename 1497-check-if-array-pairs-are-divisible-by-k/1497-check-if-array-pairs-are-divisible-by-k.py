from collections import defaultdict
class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = defaultdict(int)
        for num in arr:
            rem = num % k
            if rem < 0: rem += k
            hashmap[rem] += 1
        
        if hashmap[0] % 2 != 0:
            return False

        for num in arr:
            rem = (num % k + k) % k
            if rem != 0:
                if hashmap[rem] != hashmap[k-rem]: return False
        return True

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ptr, sub_ptr = 0, 0
        
        if s == "":
            return True
        elif  t == "":
            return False

        while ptr < len(t):
            if sub_ptr < len(s) and s[sub_ptr] == t[ptr]:
                sub_ptr += 1
            ptr += 1
        
        if sub_ptr == len(s):
            return True
        return False
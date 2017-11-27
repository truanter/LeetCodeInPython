class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        pre,cur = 0,1
        res = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                pre,cur = cur, 1
            if pre >= cur:
                res += 1
        return res

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=set(list(s))
        n,m=0,0
        for i in a:
            n += s.count(i)/2
            if s.count(i)%2==1:
                m=1
        return 2*n+m

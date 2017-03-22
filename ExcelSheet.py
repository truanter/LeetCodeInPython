class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        b=list(range(1,27))
        c=dict(zip(a,b))
        n=0
        for i in s:
            n=n*26+c[i]
        return n

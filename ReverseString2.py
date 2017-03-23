class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        b=''
        while len(s)>=2*k:
            b+=s[:k][::-1]+s[k:2*k]
            s=s[2*k:]
        if len(s)>=k:
            b+=s[:k][::-1]+s[k:]
        else:
            b+=s[::-1]
        return b

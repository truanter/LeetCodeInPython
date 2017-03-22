class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        b=[s.index(i) for i in set(s) if s.count(i)==1]
        return(min(b) if b else -1)

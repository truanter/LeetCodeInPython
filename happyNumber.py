class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l=[]
        while not n in l:
            l.append(n)
            m = 0
            for i in str(n):
                m += int(i) * int(i)
            n = m
            if n == 1:
                break
        return True if n == 1 else False

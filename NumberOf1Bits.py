class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # version 1
        c =0
        while n:
            n &= n-1
            c+=1
        return c
        # version 2
        return bin(n).count('1')

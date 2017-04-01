class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # version 1
        return not n & n-1 and n > 0
        
        # version 2
        return bin(n).count('1')==1 and n>0

class Solution(object):
    def integerBreak(self, n):
        d={1:1,2:1,3:2,4:4}
        res = 1
        if n <= 4:return d[n]
        while n>4:
            res *= 3
            n -= 3
        res *= n
        return res
        

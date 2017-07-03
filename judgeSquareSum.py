class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        i,j=0,int(math.sqrt(c))
        while i<=j:
            if i*i+j*j < c:
                i+=1
            elif i*i+j*j>c:
                j-=1
            else:
                return True
        return False
        
#another answer
def judgeSquareSum(self, c):
    def is_square(N):
        return int(N**.5)**2 == N       
    return any(is_square(c - a*a) 
                for a in xrange(int(c**.5) + 1))

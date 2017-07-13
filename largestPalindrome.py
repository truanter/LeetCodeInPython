class Solution(object):
    def largestPalindrome(self,n):
        if n==1:
            return 9
        upper = 10**n -1
        lower = 10**(n-1)
        maxnumber = upper * lower
        firstHalf = int(maxnumber/(upper+1))
        while True:
            palindrom = self.creatp(firstHalf)
            for i in reversed(range(lower,upper+1)):
                if palindrom/i > maxnumber or i*i < palindrom:
                    break
                if not palindrom % i:
                    return palindrom % 1337
            firstHalf -= 1
    def creatp(self, n):
        return int(str(n)+str(n)[::-1])

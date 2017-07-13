class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 10 : return 0
        if n == 0: return 1
        count = 9
        num=9
        for i in range(n-1):
            count *= num
            num -= 1
        return count + self.countNumbersWithUniqueDigits(n-1)

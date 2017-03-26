class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = 0
        while num:
            sum += num % 10
            num /= 10
        if sum >= 10:
            return self.addDigits(sum)
        return sum

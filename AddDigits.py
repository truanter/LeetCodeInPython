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

# Version 2 copied from others
class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        return num%9 if num%9 != 0 else 9
 '''
 100a + 10b + c % 9
 = 99a + a +9b + b +c %9
 = a + b + c %9
 '''

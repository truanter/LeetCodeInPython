class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num:
            for x in [2,3,5]:
                while not num % x:
                    num /= x
        return True if num == 1 else False

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_div(num):
            for i in list(str(num)):
                if i == '0' or num % int(i) != 0:
                    return False
            return True
        return list(filter(is_div, range(left, right+1)))

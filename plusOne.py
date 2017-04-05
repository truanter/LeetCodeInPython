class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        m = 1
        for i in range(len(digits)):
            digits[-i-1] += m
            if digits[-i-1] == 10:
                digits[-i-1] = 0
                m = 1
            else:
                m = 0
        if m:
            return [m]+digits
        else:
            return digits

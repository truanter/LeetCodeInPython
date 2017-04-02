class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=0
        l=[]
        for i in nums:
            if p < 0:
                p=i
            else:
                p+=i
            l.append(p)
        return max(l)

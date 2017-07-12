class Solution(object):
    def singleNonDuplicate(self, nums):
        l,h=0,len(nums)/2
        while l<h:
            m = (l+h)/2
            if nums[m*2]!=nums[m*2+1]:
                h = m
            else:
                l = m+1
        return nums[2*l]
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
        return res

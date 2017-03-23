class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return [i for i in set(nums) if nums.count(i)>=len(nums)/float(2)][0]

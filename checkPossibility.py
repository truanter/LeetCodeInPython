class Solution(object):
    def checkPossibility(self, nums):
        if len(nums)<2:return True
        c = 0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                c += 1
                if i<2 or nums[i-2]<=nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
            if c>1:
                return False
        return True

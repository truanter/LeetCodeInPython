class Solution(object):
    def findErrorNums(self, nums):
        res = []
        for i in nums:
            if nums[abs(i)-1]<0:
                res.append(abs(i)-1)
            else:
                nums[abs(i)-1] = -nums[abs(i)-1]
        for j in range(len(nums)):
            if nums[j]>0:
                res.append(j+1)
        return res

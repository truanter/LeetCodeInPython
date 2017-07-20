class Solution(object):
    def findMaxAverage(self, nums, k):
        i,j = 0,k
        s = sum(nums[:k])
        res = s
        while j<len(nums):
            s += nums[j]-nums[i]
            res = max(res, s)
            i += 1
            j += 1
        return res/k

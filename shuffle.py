class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        n = self.nums[:]
        for i in reversed(range(len(self.nums))):
            j = int(random.random()*len(n))
            n[i],n[j]=n[j],n[i]
        return n

'''
:type nums: List[int]
:rtype: void Do not return anything, modify nums in-place instead
'''
Class Solution(object):
    def moveZeros(self, nums):
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
            

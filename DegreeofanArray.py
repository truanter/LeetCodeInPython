class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_count_list = [[0, 0, 0] for i in range(max(nums)+1)]
        max_count = 0
        result = 1

        for i in range(len(nums)):
            nums_count_list[nums[i]][0] += 1
            if nums_count_list[nums[i]][0] == 1:
                nums_count_list[nums[i]][1] = i

            nums_count_list[nums[i]][2] = i - nums_count_list[nums[i]][1]

            if nums_count_list[nums[i]][0] > max_count:
                max_count = nums_count_list[nums[i]][0]
                result = nums_count_list[nums[i]][2] + 1
            elif nums_count_list[nums[i]][0] == max_count:
                result = min(result, nums_count_list[nums[i]][2]+1)
                
        return result

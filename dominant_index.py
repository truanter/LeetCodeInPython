class Solution:
    def dominantIndex(self, nums):
        """
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return 0
        res = nums.index(max(nums))

        if sorted(nums)[-1] >= sorted(nums)[-2] * 2:
            return res
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [3, 6, 1, 0]
    print(s.dominantIndex(nums))

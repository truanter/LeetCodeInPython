class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return -1
        if len(nums) == 1:
            return 0
        left, right = 0, sum(nums[1:])

        for i in range(1, len(nums)):
            if left == right:
                return i-1

            left += nums[i-1]
            right -= nums[i]

        return -1 if left != right else len(nums)-1


if __name__ == '__main__':
    s = Solution()
    # nums = [1, 7, 3, 6, 5, 6]
    nums = [1, 2, 3]
    print(s.pivotIndex(nums))

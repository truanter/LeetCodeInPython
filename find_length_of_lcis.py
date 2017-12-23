class Solution:
    def find_length_of_lcis(self, nums):
        """
        :param nums: List[int]
        :return:
        """
        if len(nums) == 0: return 0
        max_length = 1
        cur_length = 1

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                cur_length += 1
                max_length = max(max_length, cur_length)
            else:
                cur_length = 1

        return max_length


if __name__ == '__main__':
    s = Solution()
    print(s.find_length_of_lcis([1, 3, 5, 4, 7]))

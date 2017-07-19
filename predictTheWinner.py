class Solution(object):
    def PredictTheWinner(self, nums):
        if len(nums)<2:return True
        if self.helper(0, 0, nums, 0):
            return False
        else:
            return True
    def helper(self, val1, val2, nums, player):
        if len(nums)==2:
            if val1+max(nums) >= val2+min(nums):
                return player
            else:
                return 1-player
        if self.helper(val2, val1+nums[0], nums[1:], 1-player)==player or self.helper(val2, val1+nums[-1], nums[:-1], 1-player)==player:
            return player
        else:
            return 1-player

#version II
class Solution(object):
    def PredictTheWinner(self, nums):
        def helper(l, r, mem):
            if l>r: return 0
            if l==r: return nums[l]
            if not (l, r) in mem:
                s = sum(nums[l:r+1])
                l1,r1 = s-helper(l+1, r, mem)+nums[l], s-helper(l, r-1, mem)+nums[r]
                mem[(l,r)] = max(l1,r1)
            return mem[(l,r)]
        ss = sum(nums)
        c = helper(0, len(nums)-1, {})
        return c >= ss-c

if __name__=='__main__':
    nums = [2, 4, 55, 6, 8]
    s = Solution()
    print(s.PredictTheWinner(nums))

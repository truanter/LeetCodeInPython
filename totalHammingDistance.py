class Solution(object):
    def totalHammingDistance(self, nums):
        nums.sort(reverse = True)
        z=[0]*(len(bin(nums[0]))-2)
        o=[0]*(len(bin(nums[0]))-2)
        for i in nums:
            count = 1
            while count<= len(bin(nums[0]))-2:
                if i&1:
                    o[count-1]+=1
                else:
                    z[count-1]+=1
                count +=1
                i= i>>1
        res = 0
        print(z)
        print(o)
        for j in range(len(z)):
            res += z[j]*o[j]
        print(res)


if __name__ == '__main__':
    s = Solution()
    nums =[4,14,2]
    s.totalHammingDistance(nums)

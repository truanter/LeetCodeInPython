# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        left, right = 1, len(height) -2
        max_left, max_right = 0, 0
        ret = 0
        for i in range (1, len(height)-1):
            if height[left - 1] < height[right + 1]:
                max_left = max(height[left-1], max_left)
                if max_left > height[left]:
                    ret += max_left - height[left]
                left += 1
            else:
                max_right = max(height[right+1], max_right)
                if max_right > height[right]:
                    ret += max_right - height[right]
                right -= 1
        return ret

if __name__ == '__main__':
    l = [0,1,0,2,1,0,1,3,2,1,2,1]
    ret = Solution().trap(l)
    print(ret)
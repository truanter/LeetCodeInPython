# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        if not points:
            return 0
        l = sorted(list(set([i[0] for i in points])))
        right_bound = -1
        ret = 0
        for i in l:
            if i > right_bound:
                ret += 1
                right_bound = i + w
        return ret


if __name__ == '__main__':
    points = [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]]
    w = 1
    s = Solution()
    print(s.minRectanglesToCoverPoints(points, w))

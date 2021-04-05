# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 1:08 下午
# @Author  : hui.zhang
# @FileName: z_convert.py
# @Software: PyCharm
# @E-Mail    ：hui.zhang@cootek.cn
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ''
        skip = 2 * numRows - 2
        for i in range(numRows):
            j = i
            while j < len(s):
                res += s[j]
                middle = 2 * (numRows - i - 1)
                if not (middle == 0 or middle == skip) and j + middle < len(s):
                    res += s[j + middle]
                j += skip
        return res


if __name__ == '__main__':
    s = 'PAYPALISHIRING'
    print(Solution().convert('A', 1))
    print(Solution().convert(s, 4))

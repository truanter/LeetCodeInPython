# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 2:26 下午
# @Author  : hui.zhang
# @FileName: merge_sorted_list.py
# @Software: PyCharm
# @E-Mail    ：hui.zhang@cootek.cn
class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        cur_idx = m + n - 1
        while m and n:
            i1 = nums1[m-1]
            i2 = nums2[n-1]
            if i1 < i2:
                nums1[cur_idx] = i2
                n -= 1
            else:
                nums1[cur_idx] = i1
                m -= 1
            cur_idx -= 1
        if n:
            nums1[:n] = nums2[:n]


if __name__ == '__main__':
    l1 = [1,2,3,0,0,0]
    l2 = [2,5,6]
    Solution().merge(l1, 3, l2, 3)
    print(l1)

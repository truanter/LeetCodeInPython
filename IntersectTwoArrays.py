#Answer1
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = 0
        while n < len(nums1):
            if nums1[n] in nums2:
                nums2.remove(nums1[n])
                n += 1
            else:
                nums1.remove(nums1[n])
        return nums
#Answer 2
        a,b = set(nums1), set(nums2)
        l=[]
        for i in a:
            if i in b:
                for j in range(min(nums1.count(i), nums2.count(i))):
                    l.append(i)
        return l
#Answer 3(Copy from others)
from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        c1, c2 = Counter(nums1), Counter(nums2)
        return sum([[num] * min(c1[num], c2[num]) for num in c1 & c2], [])

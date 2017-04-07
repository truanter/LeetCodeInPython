class Solution(object):
    def guessNumber(self, n):
        l,h = 1,n
        while h>=l:
            mid = (l+h)/2
            r = guess(mid)
            if not r:
                return mid
            elif r == -1:
                h = mid-1
            else:
                l = mid+1

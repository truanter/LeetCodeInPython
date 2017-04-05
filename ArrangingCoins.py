class Solution(object):
    def arrangeCoins(self, n):
        return int((8*n +1)**0.5-1)/2

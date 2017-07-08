class Solution:
    def distributeCandies(self, candies):
        return min(len(set(candies)), int(len(candies)/2))

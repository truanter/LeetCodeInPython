class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if prices:
            min = prices[0]
            for i in prices:
                if i < min:
                    min = i
                else:
                    if i - min > profit:
                        profit = i - min
        return profit

def maxProfit(prices):
    l=[prices[i+1]-prices[i] for i in range(len(prices)-1) if prices[i+1]-prices[i]>=0]
    return sum(l)

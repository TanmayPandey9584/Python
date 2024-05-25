class Solution:
    def maxProfit(self, prices):
        if prices.index(min(prices))==len(prices):
            print(0)
        else:
            print(max(prices[prices.index(min(prices)):len(prices)])-prices.index(min(prices)))

a=Solution()
prices=[7,1,5,3,6,4]
a.maxProfit(prices)

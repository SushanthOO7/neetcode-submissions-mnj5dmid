class Solution:
    def maxProfit(self, a: List[int]) -> int:
        maxP = 0
        minBuy = a[0]

        for sell in a:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP
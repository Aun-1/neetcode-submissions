class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0
        minb=prices[0]

        for n in prices:
            maxP=max(maxP,n-minb)
            minb=min(minb,n)
        return maxP
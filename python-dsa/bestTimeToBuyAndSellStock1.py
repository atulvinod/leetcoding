from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxp = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                maxp = max(prices[right] - prices[left], maxp)
            else:
                left = right
            right += 1
        return maxp
                

Solution().maxProfit(prices = [7,1,5,3,6,4])
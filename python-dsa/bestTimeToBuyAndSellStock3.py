class Solution:
    def solve(self, prices, day, transactions_left, memo):
        if day == len(prices):
            return 0

        if transactions_left == 0:
            return 0

        ans = memo[day][transactions_left]

        if ans != -1:
            return ans

        # Choice 1: No transaction today
        ans1 = self.solve(prices, day + 1, transactions_left, memo)

        # Choice 2: Doing the possible transaction today
        ans2 = 0
        buy = transactions_left % 2 == 0

        if buy:  # Buy
            ans2 = -prices[day] + self.solve(prices, day + 1, transactions_left - 1, memo)
        else:  # Sell
            ans2 = prices[day] + self.solve(prices, day + 1, transactions_left - 1, memo)

        ans = max(ans1, ans2)
        memo[day][transactions_left] = ans  # Store ans in memo before returning
        return ans

    def max_profit(self, prices):
        memo = [[-1] * 5 for _ in range(len(prices))]
        ans = self.solve(prices, 0, 4, memo)
        return ans

# Example usage:
sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
result = sol.max_profit(prices)
print(result)

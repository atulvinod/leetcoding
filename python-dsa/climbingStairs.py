class Solution:
    def compute(self):
        dp = [None] * 46
        dp[0] = 1
        dp[1] = 2
        for i in range(2, 46):
            dp[i] = dp[i-1] + dp[i - 2]
        return dp
    def climbStairs(self, n: int) -> int:
        dp = self.compute()
        return dp[n-1]
        

Solution().climbStairs(3)
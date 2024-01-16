class Solution:
    def numSquares(self, n: int) -> int:
        possibleNumbers = []
        i = 1;
        while (i**2 < n):
            possibleNumbers.append(i**2)
            i += 1
        dp = dict()
        def solve(target):
            if target == 0:
                return 0
            if target < 0:
                return float('inf')
            if target in dp:
                return dp[target]
            
            minSteps = float('inf')
            for p in possibleNumbers:
                minSteps = min(minSteps, solve(target - p))
            dp[target] =  1 + minSteps
            return dp[target]
        result = solve(n)
        return result

Solution().numSquares(13)
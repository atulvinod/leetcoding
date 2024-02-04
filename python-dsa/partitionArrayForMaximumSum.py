from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        memo = dict()
        def solve(arrayStart):
            nonlocal memo
            if arrayStart >= len(arr):
                return 0
            
            if arrayStart in memo:
                return memo[arrayStart]
            
            result = -float('inf')
            currentMax = arr[arrayStart]
            for i in range(arrayStart, min(arrayStart+k, len(arr))):
                currentMax = max(currentMax, arr[i])
                currentWindowSum = (currentMax*(i - arrayStart+1))+solve(i+1)    
                result = max(result, currentWindowSum)
            memo[arrayStart] = result
            return result
            
        result = solve(0)
        return result
Solution().maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3)    
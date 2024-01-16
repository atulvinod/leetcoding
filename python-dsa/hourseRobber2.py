from typing import List

'''
This problem is an extension of House Robber 1, here the condition is that the arrangement is circular, that is that if we select the first house, then the last house is invalid, and if we choose the last house,
then the first house is invalid, hence we run two normal house robber functions where we skip the first house and the other where we skip the last house
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def solve(current , end, dp):
            if current > end:
                return 0
            if current in dp:
                return dp[current]

            take = nums[current] + solve(current+2, end, dp)
            dontTake = solve(current+1, end ,dp)
            dp[current] = max(take,dontTake)
            return dp[current]
        
        a = solve(0, len(nums)-2, dict())
        b = solve(1, len(nums) - 1, dict())
        return max(a, b)

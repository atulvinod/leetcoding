from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        memo = dict()
        def solve(index: int, currentSet: List[int], mask):
            nonlocal result
            if index >= len(nums):
                if len(currentSet) > len(result):
                    result = currentSet[:]
                return
            ifmme
            
            if len(currentSet) == 0 or (currentSet[-1] % nums[index] == 0) or (nums[index] % currentSet[-1]) == 0:
                currentSet.append(nums[index])
                mask = mask | 1 << index
                solve(index+1, currentSet, mask)
                mask  = mask & ~(1 << index)
                currentSet.pop()

            solve(index+1, currentSet, mask)
        solve(0,[], 0)
        return result
    
Solution().largestDivisibleSubset([1,2,4,8])
        
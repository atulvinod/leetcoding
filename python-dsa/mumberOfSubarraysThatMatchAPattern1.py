from typing import List

class Solution:

    def patternMatch(self, nums, pattern, i, k):
        patternVal = pattern[k]
        if i+1 >= len(nums) or i+1+k >= len(nums):
            return False
        if patternVal == 1 and nums[i+1+k] > nums[i+k]:
            return True
        if patternVal == 0 and nums[i+1+k] == nums[i+k]:
            return True
        if patternVal == -1 and nums[i+k+1] < nums[i+k]:
            return True
        return False
     
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        result = 0

        for i in range(len(nums)):
            j = 0
            while j < len(pattern) and self.patternMatch(nums, pattern, i, j):
                j+=1
            if j == len(pattern):
                result += 1

        return result        
    

Solution().countMatchingSubarrays(nums = [1,2,3,4,5,6], pattern = [1,1])
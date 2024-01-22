from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)+1):
            if nums[i-1] != i:
                return [nums[i-1], i]
        return []
    
    
print(Solution().findErrorNums([2,2]))
from typing import List

class Solution: 
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        globalMax = -1
        prefixSum = [0]*(len(nums)+1)
        for i in range(0, len(nums)):
            prefixSum[i+1] = nums[i]+prefixSum[i]

        print(prefixSum)
        for index in range(3, len(prefixSum)):
            if prefixSum[index-1] > nums[index-1]:
                globalMax = max(prefixSum[index], globalMax)

        return globalMax

Solution().largestPerimeter(nums = [5,5,5])
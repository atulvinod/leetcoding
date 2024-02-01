from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        tempArray = []
        for i in range(len(nums)):
            if len(tempArray) == 0 or (nums[i] - tempArray[0] <= k and len(tempArray) != 3):
                tempArray.append(nums[i])
            else:
                if len(tempArray) != 3:
                    return []
                result.append(tempArray)
                tempArray = [nums[i]]
        if len(tempArray) != 0:
            result.append(tempArray)
        return result
    
Solution().divideArray(nums = [1,3,3,2,7,3], k = 3)
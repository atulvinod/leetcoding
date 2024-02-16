from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positiveNumbers = []
        negativeNumbers = []
        result = []

        for i in nums:
            if i < 0:
                negativeNumbers.append(i)
            else:
                positiveNumbers.append(i)
        
        takePositive = True
        i, j = 0,0
        while i < len(positiveNumbers)  and j < len(negativeNumbers):
            if takePositive:
                result.append(positiveNumbers[i])
                i += 1
            else:
                result.append(negativeNumbers[j])
                j += 1
            takePositive = not takePositive
        
        while i < len(positiveNumbers):
            result.append(positiveNumbers[i])
            i += 1
        while j < len(negativeNumbers):
            result.append(negativeNumbers[j])
            j += 1

        return result

Solution().rearrangeArray([3,1,-2,-5,2,-4])
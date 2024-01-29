'''
#important
'''
from typing import List
from collections import Counter
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        maxLength = 1
        valueCount = Counter(nums)
        uniqueNumbers = sorted(valueCount.keys())
        for number in uniqueNumbers:
            if number == 1:
                if valueCount[number] % 2 == 0:
                    maxLength = max(maxLength, valueCount[number] - 1)
                else:
                    maxLength = max(maxLength, valueCount[number])

            elif valueCount[number] >= 2:
                previousNumber = number
                currentLength = 2
                while True:
                    if previousNumber ** 2 in valueCount:
                        if valueCount[previousNumber ** 2] == 1:
                            currentLength += 1
                            break
                        else:
                            if (currentLength + 1) % 2 != 0:
                                maxLength = max(currentLength+1, maxLength)
                            
                            currentLength += 2
                            previousNumber = previousNumber**2
                    else:
                        break
                if currentLength % 2 != 0:
                    maxLength = max(currentLength, maxLength)
        return maxLength                        

Solution().maximumLength([14,14,196,196,38416,38416])